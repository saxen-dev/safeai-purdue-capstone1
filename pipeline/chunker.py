"""
Smart chunking: semantic chunks from extracted content with BM25 index.
"""

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Any

from rank_bm25 import BM25Okapi

from .config import ExtractionConfig, PreservationLevel

# ---------------------------------------------------------------------------
# Clinical metadata — drug name vocabulary
# ---------------------------------------------------------------------------
# Used to identify drug names in table headers and NLL text.
_KNOWN_DRUG_NAMES = frozenset([
    "artemether", "lumefantrine", "artesunate", "amodiaquine", "mefloquine",
    "sulfadoxine", "pyrimethamine", "primaquine", "dihydroartemisinin",
    "piperaquine", "quinine", "chloroquine", "amoxicillin", "cotrimoxazole",
    "metronidazole", "ciprofloxacin", "doxycycline", "penicillin",
    "gentamicin", "ampicillin", "erythromycin", "fluconazole",
    "paracetamol", "ibuprofen", "prednisolone", "insulin",
    "salbutamol", "metformin", "zinc",
])

# ---------------------------------------------------------------------------
# Clinical metadata — compiled regex patterns
# ---------------------------------------------------------------------------

_FREQUENCY_RE = re.compile(
    r'\b(once|twice|three\s+times|four\s+times)\s+(?:a\s+)?daily\b', re.I
)
_DURATION_RE = re.compile(r'\bfor\s+(\d+)\s+(days?|weeks?)\b', re.I)
_ROUTE_RE = re.compile(
    r'\b(oral(?:ly)?|intravenous(?:ly)?|IV|intramuscular(?:ly)?|IM'
    r'|rectal(?:ly)?|subcutaneous(?:ly)?|topical(?:ly)?)\b', re.I
)
_LOC_RE = re.compile(
    r'\b(HC\s*[IVX]{1,4}|HC\s*[2-5]|hospital|health\s+cent(?:er|re)'
    r'|district\s+hospital|referral\s+hospital|outpatient|inpatient)\b', re.I
)
_CONTRAINDICATION_RE = re.compile(
    r'contraindicated?\s+in\s+([^.;]{5,80})', re.I
)
_DO_NOT_GIVE_RE = re.compile(
    r'(?:do\s+not\s+give|not\s+recommended\s+for)\s+([^.;]{5,80})', re.I
)
_DANGER_SIGN_RE = re.compile(
    r'danger\s+signs?\s*[;:–-]\s*([^.;]{5,150})', re.I
)
_REFERRAL_RE = re.compile(
    r'refer\s+(?:immediately|urgently|directly)?\s*(?:if|when|to|for)\s+([^.;]{5,100})',
    re.I,
)
_CLINICAL_FEATURES_RE = re.compile(
    r'(?:clinical\s+features?|signs?\s+and\s+symptoms?)\s*[:;–]\s*([^.]{10,200})',
    re.I,
)
_SPECIAL_POP_RE = re.compile(
    r'\b(pregnant\s+wom(?:an|en)|lactating\s+moth(?:er|ers?)'
    r'|(?:infants?|neonates?|children)\s+(?:under|<|≤)\s*\d+\s*(?:kg|months?|years?)'
    r'|HIV(?:\s+positive)?|immunocompromised)\b',
    re.I,
)
_AGE_MIN_RE = re.compile(
    r'(?:adults?|patients?)\s*[>≥]\s*(\d+)\s*(years?|months?)', re.I
)
_AGE_MAX_RE = re.compile(
    r'(?:children|infants?|neonates?)\s*(?:under|<|≤)\s*(\d+)\s*(years?|months?)', re.I
)
_WEIGHT_RANGE_RE = [
    re.compile(r'(\d+\.?\d*)\s*[-–to<≤]+\s*<?(\d+\.?\d*)\s*kg', re.I),
    re.compile(r'[>≥]\s*=?\s*(\d+\.?\d*)\s*kg', re.I),
    re.compile(r'^[<≤]\s*(\d+\.?\d*)\s*kg', re.I),
]


def _parse_weight_range_from_cell(cell: str):
    """Return (lo_kg, hi_kg|None) from a weight cell string, or None."""
    cell = cell.strip()
    m = re.search(r'[>≥]\s*=?\s*(\d+\.?\d*)', cell)
    if m:
        return (float(m.group(1)), None)
    m = re.search(r'(\d+\.?\d*)\s*[-–to<≤]+\s*<?(\d+\.?\d*)', cell)
    if m:
        return (float(m.group(1)), float(m.group(2)))
    m = re.search(r'^[<≤]\s*(\d+\.?\d*)', cell)
    if m:
        return (0.0, float(m.group(1)))
    return None


def _normalize_loc(raw: str) -> str:
    """Normalise level-of-care strings: 'HC III' → 'HC3', etc."""
    raw = raw.strip()
    roman = {"I": "1", "II": "2", "III": "3", "IV": "4", "V": "5"}
    m = re.match(r'HC\s*([IVX]+)', raw, re.I)
    if m:
        return "HC" + roman.get(m.group(1).upper(), m.group(1))
    m = re.match(r'HC\s*([2-5])', raw, re.I)
    if m:
        return "HC" + m.group(1)
    return raw.strip()


# ---------------------------------------------------------------------------
# Parent-child chunking — token budget constants
# ---------------------------------------------------------------------------
_TOKEN_MULTIPLIER = 1.3
_CHILD_MAX_TOKENS = 512
_CHILD_OVERLAP_TOKENS = 50
_CHILD_MIN_TOKENS = 50


def _estimate_tokens(text: str) -> int:
    """Approximate token count from word count (1.3× multiplier)."""
    return int(len(text.split()) * _TOKEN_MULTIPLIER)


def _split_recursive_paragraph(
    text: str,
    max_tokens: int = _CHILD_MAX_TOKENS,
    overlap_tokens: int = _CHILD_OVERLAP_TOKENS,
    min_tokens: int = _CHILD_MIN_TOKENS,
) -> List[str]:
    """
    Split text on paragraph → sentence → word boundaries.

    Builds chunks up to max_tokens, flushes and starts a new chunk when
    adding the next paragraph would exceed the limit.  Long single paragraphs
    are further split at sentence boundaries.  Consecutive chunks receive an
    overlap prefix taken from the tail of the previous chunk.
    """
    paragraphs = re.split(r"\n\n+", text.strip())
    chunks: List[str] = []
    current: List[str] = []
    current_tokens = 0

    for para in paragraphs:
        pt = _estimate_tokens(para)
        if current_tokens + pt <= max_tokens:
            current.append(para)
            current_tokens += pt
        else:
            if current:
                chunks.append("\n\n".join(current))
            if pt > max_tokens:
                sentences = re.split(r"(?<=[.!?])\s+", para)
                sent_chunk: List[str] = []
                sent_tokens = 0
                for sent in sentences:
                    st = _estimate_tokens(sent)
                    if sent_tokens + st <= max_tokens:
                        sent_chunk.append(sent)
                        sent_tokens += st
                    else:
                        if sent_chunk:
                            chunks.append(" ".join(sent_chunk))
                        sent_chunk = [sent]
                        sent_tokens = st
                if sent_chunk:
                    current = [" ".join(sent_chunk)]
                    current_tokens = _estimate_tokens(current[0])
                else:
                    current = []
                    current_tokens = 0
            else:
                current = [para]
                current_tokens = pt

    if current:
        chunks.append("\n\n".join(current))

    chunks = [c for c in chunks if _estimate_tokens(c) >= min_tokens]

    if overlap_tokens > 0 and len(chunks) > 1:
        overlap_words = int(overlap_tokens / _TOKEN_MULTIPLIER)
        overlapped = [chunks[0]]
        for i in range(1, len(chunks)):
            tail = " ".join(chunks[i - 1].split()[-overlap_words:])
            overlapped.append(tail + " " + chunks[i])
        chunks = overlapped

    return chunks if chunks else [text]


def _decompose_propositions(
    text: str,
    max_tokens: int = 200,
    min_tokens: int = 30,
) -> List[str]:
    """
    Sentence-level decomposition for verbatim-preservation chunks.

    Each output proposition is independently retrievable — critical for
    safety content (danger signs, referral criteria, dosing rules) where
    a single sentence carries a complete clinical fact.
    """
    sentences = re.split(r"(?<=[.!?:;])\s+", text.strip())
    propositions: List[str] = []
    current: List[str] = []
    current_tokens = 0

    for sent in sentences:
        st = _estimate_tokens(sent)
        if current_tokens + st <= max_tokens:
            current.append(sent)
            current_tokens += st
        else:
            if current:
                propositions.append(" ".join(current))
            current = [sent]
            current_tokens = st

    if current:
        propositions.append(" ".join(current))

    merged: List[str] = []
    for prop in propositions:
        if merged and _estimate_tokens(prop) < min_tokens:
            merged[-1] = merged[-1] + " " + prop
        else:
            merged.append(prop)

    return merged if merged else [text]


# ---------------------------------------------------------------------------
# Keywords used to infer section_type from heading text.
# Short tokens (mg, kg) use word-boundary matching to avoid false substring hits
# (e.g. "kg" inside "background").  Longer tokens use plain substring matching.
_DOSING_KEYWORDS_LONG = {"dose", "dosing", "dosage", "regimen", "schedule", "tablet"}
_DOSING_KEYWORDS_SHORT = {"mg", "kg"}  # matched as whole words only
_DIAGNOSIS_KEYWORDS = {"diagnosis", "diagnostic", "symptom", "sign", "test", "laboratory", "criteria"}
_TREATMENT_KEYWORDS = {"treatment", "management", "therapy", "protocol", "intervention", "prophylaxis"}
_CONTRAINDICATION_KEYWORDS = {"contraindication", "warning", "caution", "adverse", "side effect", "precaution"}


class SmartChunker:
    """
    Creates semantic chunks from extracted content.
    Preserves document structure and medical context.
    """

    def __init__(self, extraction_result: Dict, config: ExtractionConfig):
        self.extraction = extraction_result
        self.config = config
        self.chunks: List[Dict] = []
        self.children: List[Dict] = []
        self.chunk_index: Dict[str, Any] = {}
        self._image_by_page: Dict[int, List[Dict]] = self._load_image_inventory()

    # ------------------------------------------------------------------
    # Metadata inference helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _infer_section_type(heading: str, is_table_only: bool = False) -> str:
        """Infer a coarse section type from heading text."""
        if is_table_only:
            return "table"
        h = heading.lower()
        # Use substring matching so plurals/suffixes (e.g. "contraindications") still match.
        # Short tokens use word-boundary matching to avoid false hits (e.g. "kg" in "background").
        _short_word_match = bool(re.search(r"\b(?:mg|kg)\b", h))
        if any(kw in h for kw in _DOSING_KEYWORDS_LONG) or _short_word_match:
            return "dosing"
        if any(kw in h for kw in _CONTRAINDICATION_KEYWORDS):
            return "contraindication"
        if any(kw in h for kw in _DIAGNOSIS_KEYWORDS):
            return "diagnosis"
        if any(kw in h for kw in _TREATMENT_KEYWORDS):
            return "treatment"
        return "background"

    @staticmethod
    def _infer_preservation_level(
        section_type: str, has_tables: bool
    ) -> PreservationLevel:
        """Infer how faithfully this chunk's text must be preserved in responses."""
        if section_type in ("table", "dosing"):
            return PreservationLevel.VERBATIM
        if has_tables or section_type in ("contraindication", "treatment"):
            return PreservationLevel.HIGH
        return PreservationLevel.STANDARD

    # ------------------------------------------------------------------
    # Image OCR enrichment
    # ------------------------------------------------------------------

    def _load_image_inventory(self) -> Dict[int, List[Dict]]:
        """
        Build a page → [image_data, …] mapping from image_inventory.json.

        Looks first in the extraction dict (key "image_inventory"), then in
        config.output_dir/image_inventory.json.  Returns an empty dict when
        no inventory is available — callers always use .get(page, []).
        """
        images: List[Dict] = self.extraction.get("image_inventory", [])
        if not images and getattr(self.config, "output_dir", None):
            img_path = Path(self.config.output_dir) / "image_inventory.json"
            if img_path.exists():
                with open(img_path, encoding="utf-8") as fh:
                    images = json.load(fh)
        by_page: Dict[int, List[Dict]] = defaultdict(list)
        for img in images:
            pg = img.get("page_no")
            if pg is not None:
                by_page[int(pg)].append(img)
        return dict(by_page)

    def _build_image_chunk(self, page_num: int, image_data: Dict) -> Dict:
        """
        Build a chunk for a single image.

        When image_data carries OCR text or a caption (from Stage 1 extraction),
        the chunk gets real content and content_type="image_ocr".  Otherwise it
        is a placeholder so downstream code can still see the image exists.
        """
        ocr_text = (image_data.get("ocr_text") or "").strip()
        caption = (image_data.get("caption") or "").strip()
        parts: List[str] = []
        if caption:
            parts.append(f"[Image caption: {caption}]")
        if ocr_text:
            parts.append(ocr_text)
        content = "\n".join(parts) if parts else "<!-- image -->"
        content_type = "image_ocr" if parts else "image_placeholder"

        chunk: Dict[str, Any] = {
            "chunk_id": f"chunk_image_{len(self.chunks):06d}",
            "page": page_num,
            "heading": caption or "Image",
            "level": 3,
            "text": content,
            "tables": [],
            "has_tables": False,
            "char_count": len(content),
            "word_count": len(content.split()),
            "section_type": "background",
            "preservation_level": PreservationLevel.STANDARD.value,
            "content_type": content_type,
            "image_path": image_data.get("saved_path", ""),
            "related_chunk_ids": [],
        }
        # Only run metadata extraction when there is real OCR text to parse.
        if content_type == "image_ocr":
            chunk["clinical_metadata"] = self._extract_clinical_metadata(chunk)
        else:
            chunk["clinical_metadata"] = self._empty_clinical_metadata()
        return chunk

    # ------------------------------------------------------------------
    # Clinical metadata extraction
    # ------------------------------------------------------------------

    @staticmethod
    def _empty_clinical_metadata() -> Dict:
        """Return a blank 17-field clinical metadata dict."""
        return {
            "condition": None,
            "drug_name": None,
            "dosage_summary": None,
            "patient_weight_min_kg": None,
            "patient_weight_max_kg": None,
            "patient_age_min": None,
            "patient_age_max": None,
            "route": None,
            "frequency": None,
            "duration": None,
            "contraindications": [],
            "special_populations": [],
            "level_of_care": [],
            "clinical_features": [],
            "danger_signs": [],
            "referral_criteria": [],
            "clinical_section_type": None,
        }

    @staticmethod
    def _extract_clinical_metadata(chunk: Dict) -> Dict:
        """
        Populate all 17 clinical metadata fields for a chunk.

        Dispatches by table classification:
          - dosing tables  → drug_name, weight min/max, frequency, duration, route
          - clinical tables → level_of_care, danger_signs, referral_criteria
        Narrative regex runs on combined text for all chunk types.
        """
        meta = SmartChunker._empty_clinical_metadata()
        text = chunk.get("text", "")
        tables = chunk.get("tables", [])
        heading = chunk.get("heading", "")
        section_type = chunk.get("section_type", "background")

        meta["clinical_section_type"] = section_type

        # Condition from heading (strip markdown #s)
        heading_clean = re.sub(r'^#+\s*', '', heading).strip()
        if heading_clean and heading_clean.lower() not in ("untitled", "table"):
            meta["condition"] = heading_clean

        # Build combined text corpus (chunk text + table markdown + NLL)
        full_text = text
        for t in tables:
            full_text += " " + t.get("markdown", "") + " " + t.get("nll", "")

        # --- dosing table fields ---
        dosing_tables = [t for t in tables if t.get("classification") == "dosing"]
        if dosing_tables:
            # Drug name: scan headers + NLL for known drug names
            for t in dosing_tables:
                headers_str = " ".join(str(h).lower() for h in t.get("headers", []))
                nll_lower = t.get("nll", "").lower()
                combined = headers_str + " " + nll_lower
                for drug in _KNOWN_DRUG_NAMES:
                    if drug in combined:
                        meta["drug_name"] = drug
                        break
                if meta["drug_name"]:
                    break

            # Weight min/max across all rows
            weight_mins: List[float] = []
            weight_maxes: List[float] = []
            for t in dosing_tables:
                headers = [str(h) for h in t.get("headers", [])]
                weight_col_indices = [
                    i for i, h in enumerate(headers)
                    if any(kw in h.lower() for kw in ["weight", "body weight"])
                ]
                for row in t.get("data", []):
                    cells: List[str] = []
                    if isinstance(row, dict):
                        cells = [str(row.get(h, "")) for h in headers]
                    else:
                        cells = [str(v) for v in row]
                    for idx in weight_col_indices:
                        if idx < len(cells):
                            parsed = _parse_weight_range_from_cell(cells[idx])
                            if parsed:
                                lo, hi = parsed
                                weight_mins.append(lo)
                                if hi is not None:
                                    weight_maxes.append(hi)
            if weight_mins:
                meta["patient_weight_min_kg"] = min(weight_mins)
            if weight_maxes:
                meta["patient_weight_max_kg"] = max(weight_maxes)

        # --- frequency and duration ---
        m = _FREQUENCY_RE.search(full_text)
        if m:
            meta["frequency"] = m.group(0).lower().strip()
        m = _DURATION_RE.search(full_text)
        if m:
            meta["duration"] = f"for {m.group(1)} {m.group(2).lower()}"
        if meta["frequency"] or meta["duration"]:
            meta["dosage_summary"] = ", ".join(
                p for p in [meta["frequency"], meta["duration"]] if p
            )

        # --- route ---
        m = _ROUTE_RE.search(full_text)
        if m:
            meta["route"] = m.group(0).lower().strip()
        elif dosing_tables:
            meta["route"] = "oral"  # safe default for ACT / oral guideline drugs

        # --- level of care ---
        locs = [_normalize_loc(m.group(0)) for m in _LOC_RE.finditer(full_text)]
        meta["level_of_care"] = list(dict.fromkeys(locs))

        # --- danger signs ---
        meta["danger_signs"] = [
            m.group(1).strip() for m in _DANGER_SIGN_RE.finditer(full_text)
        ]

        # --- referral criteria ---
        meta["referral_criteria"] = [
            m.group(1).strip() for m in _REFERRAL_RE.finditer(full_text)
        ]

        # --- clinical features ---
        meta["clinical_features"] = [
            m.group(1).strip() for m in _CLINICAL_FEATURES_RE.finditer(full_text)
        ]

        # --- contraindications ---
        ci = [m.group(1).strip() for m in _CONTRAINDICATION_RE.finditer(full_text)]
        ci += [m.group(1).strip() for m in _DO_NOT_GIVE_RE.finditer(full_text)]
        meta["contraindications"] = ci

        # --- special populations ---
        meta["special_populations"] = list(dict.fromkeys(
            m.group(0).strip() for m in _SPECIAL_POP_RE.finditer(full_text)
        ))

        # --- patient age ---
        m = _AGE_MIN_RE.search(full_text)
        if m:
            meta["patient_age_min"] = f"{m.group(1)} {m.group(2).lower()}"
        m = _AGE_MAX_RE.search(full_text)
        if m:
            meta["patient_age_max"] = f"{m.group(1)} {m.group(2).lower()}"

        return meta

    def _link_related_chunks(self) -> None:
        """
        Populate related_chunk_ids and related_chunks on every chunk.

        Three passes — must run after all chunks (text, table, image) are built:

        Pass 1 — sequential prev/next siblings (by array order).
        Pass 2 — table/image ↔ nearest narrative: non-narrative chunks get
                 preceding_narrative / following_narrative; narrative chunks
                 accumulate context_for_tables for every non-narrative that
                 points back at them.
        Pass 3 — section siblings: all chunks sharing the same heading are
                 listed in each other's section_siblings.
        """
        chunks = self.chunks
        if not chunks:
            return

        def _is_non_narrative(c: Dict) -> bool:
            return (
                c.get("is_table_only", False)
                or c.get("content_type") in ("image_ocr", "image_placeholder")
            )

        # Initialise related_chunks on every chunk (idempotent re-run safe).
        for chunk in chunks:
            chunk["related_chunks"] = {
                "prev_sibling": None,
                "next_sibling": None,
                "preceding_narrative": None,
                "following_narrative": None,
                "context_for_tables": [],
                "section_siblings": [],
            }

        # Pass 1: sequential prev / next.
        for i, chunk in enumerate(chunks):
            if i > 0:
                chunk["related_chunks"]["prev_sibling"] = chunks[i - 1]["chunk_id"]
            if i < len(chunks) - 1:
                chunk["related_chunks"]["next_sibling"] = chunks[i + 1]["chunk_id"]

        # Pass 2: table/image ↔ narrative proximity.
        for i, chunk in enumerate(chunks):
            if not _is_non_narrative(chunk):
                continue
            # Nearest preceding narrative (walk backward).
            for j in range(i - 1, -1, -1):
                if not _is_non_narrative(chunks[j]):
                    chunk["related_chunks"]["preceding_narrative"] = chunks[j]["chunk_id"]
                    chunks[j]["related_chunks"]["context_for_tables"].append(chunk["chunk_id"])
                    break
            # Nearest following narrative (walk forward).
            for j in range(i + 1, len(chunks)):
                if not _is_non_narrative(chunks[j]):
                    chunk["related_chunks"]["following_narrative"] = chunks[j]["chunk_id"]
                    break

        # Pass 3: section siblings grouped by heading.
        section_groups: Dict[str, List[str]] = defaultdict(list)
        for chunk in chunks:
            section_groups[chunk.get("heading", "")].append(chunk["chunk_id"])
        for chunk in chunks:
            key = chunk.get("heading", "")
            chunk["related_chunks"]["section_siblings"] = [
                cid for cid in section_groups[key] if cid != chunk["chunk_id"]
            ]

        # Sync flat related_chunk_ids (all related IDs, deduped, in order).
        for chunk in chunks:
            rc = chunk["related_chunks"]
            ids: List[str] = []
            for field in ("prev_sibling", "next_sibling", "preceding_narrative", "following_narrative"):
                if rc[field]:
                    ids.append(rc[field])
            ids.extend(rc["context_for_tables"])
            ids.extend(rc["section_siblings"])
            chunk["related_chunk_ids"] = list(dict.fromkeys(ids))

    # ------------------------------------------------------------------
    # Parent-child chunking Phase 2
    # ------------------------------------------------------------------

    @staticmethod
    def _build_contextual_header(chunk: Dict, doc_title: str = "") -> str:
        """
        Build a retrieval context header from chunk metadata.

        The header is prepended to each child's text to form
        ``contextual_content`` — the string embedded and BM25-indexed so the
        retriever sees both the clinical context (condition, drug, source) and
        the raw content in a single unit.
        """
        parts: List[str] = []
        heading = chunk.get("heading", "")
        if heading and heading.lower() not in ("untitled", "image"):
            parts.append(heading)
        cm = chunk.get("clinical_metadata") or {}
        condition = cm.get("condition")
        if condition and condition != heading:
            parts.append(condition)
        drug = cm.get("drug_name")
        if drug:
            parts.append(drug)
        src_parts: List[str] = []
        if doc_title:
            src_parts.append(doc_title)
        page = chunk.get("page")
        if page:
            src_parts.append(f"p.{page}")
        if src_parts:
            parts.append(f"Source: {' '.join(src_parts)}")
        return f"[Context: {' | '.join(parts)}]" if parts else ""

    def create_child_chunks(self, doc_title: str = "") -> List[Dict]:
        """
        Split parent chunks into smaller child chunks for dense retrieval.

        Three-layer contextual retrieval architecture:
          1. Contextual header (metadata summary) prepended to every child.
          2. Child content — routed by preservation level:
               VERBATIM  → proposition decomposition (≤200 tokens each)
               HIGH      → recursive paragraph split (≤400 tokens)
               STANDARD  → recursive paragraph split (≤512 tokens)
          3. Dosing-table parents get an extra NLL child for natural-language
             search alongside the verbatim table child.

        Image placeholders are skipped; OCR image chunks get a single child.

        Populates ``self.children`` and returns it.
        """
        children: List[Dict] = []
        counter = 0

        def _make_child(
            parent: Dict,
            text: str,
            *,
            suffix: str = "",
            is_nll: bool = False,
        ) -> Dict:
            nonlocal counter
            counter += 1
            header = self._build_contextual_header(parent, doc_title)
            contextual = f"{header}\n\n{text}" if header else text
            pid = parent["chunk_id"]
            return {
                "chunk_id": f"child_{pid}_{counter:04d}",
                "parent_chunk_id": pid,
                "text": text,
                "contextual_content": contextual,
                "page": parent.get("page", 0),
                "heading": parent.get("heading", ""),
                "section_type": parent.get("section_type", "background"),
                "preservation_level": parent.get("preservation_level",
                                                  PreservationLevel.STANDARD.value),
                "tables": [],
                "has_tables": False,
                "is_table_only": False,
                "is_nll": is_nll,
                "content_type": parent.get("content_type"),
                "image_path": parent.get("image_path", ""),
                "char_count": len(text),
                "word_count": len(text.split()),
                "clinical_metadata": parent.get("clinical_metadata",
                                                 self._empty_clinical_metadata()),
                "related_chunk_ids": [],
                "related_chunks": parent.get("related_chunks", {}),
            }

        for parent in self.chunks:
            text = parent.get("text", "")
            pres = parent.get("preservation_level", PreservationLevel.STANDARD.value)
            content_type = parent.get("content_type")
            is_table = parent.get("is_table_only", False)

            # Image placeholders — skip entirely.
            if content_type == "image_placeholder":
                continue

            # Image OCR — one child carrying the OCR text.
            if content_type == "image_ocr":
                if text.strip() and _estimate_tokens(text) >= _CHILD_MIN_TOKENS:
                    children.append(_make_child(parent, text, suffix="ocr"))
                continue

            # Standalone table chunks.
            if is_table:
                children.append(_make_child(parent, text, suffix="table"))
                # Extra NLL child for dosing tables (natural-language search).
                if parent.get("section_type") in ("table", "dosing"):
                    for t in parent.get("tables", []):
                        nll = (t.get("nll") or "").strip()
                        if nll:
                            children.append(_make_child(parent, nll,
                                                        suffix="nll", is_nll=True))
                            break  # one NLL child per table chunk
                continue

            # Narrative chunks — route by preservation level.
            token_est = _estimate_tokens(text)

            if pres == PreservationLevel.VERBATIM.value:
                for i, prop in enumerate(_decompose_propositions(text)):
                    children.append(_make_child(parent, prop, suffix=f"prop{i}"))

            elif pres == PreservationLevel.HIGH.value:
                if token_est <= 400:
                    children.append(_make_child(parent, text))
                else:
                    for i, part in enumerate(
                        _split_recursive_paragraph(text, max_tokens=400,
                                                   overlap_tokens=_CHILD_OVERLAP_TOKENS)
                    ):
                        children.append(_make_child(parent, part, suffix=f"part{i}"))

            else:  # STANDARD
                if token_est <= _CHILD_MAX_TOKENS:
                    children.append(_make_child(parent, text))
                else:
                    for i, part in enumerate(
                        _split_recursive_paragraph(text)
                    ):
                        children.append(_make_child(parent, part, suffix=f"part{i}"))

        self.children = children
        ratio = f"{len(children)}/{len(self.chunks)}" if self.chunks else "0/0"
        print(f"  Created {len(children)} child chunks from {len(self.chunks)} parents"
              f" ({ratio} ratio)")
        return children

    def chunk_by_headings(self) -> List[Dict]:
        """Create chunks based on document headings."""
        print("\n🧩 Creating semantic chunks...")

        for page in self.extraction.get("pages", []):
            sections = self._group_by_headings(page)

            for section in sections:
                chunk = self._build_chunk(section, page["page"])
                if chunk:
                    self.chunks.append(chunk)

            # Enrich image chunks for this page with Stage 1 OCR data.
            for img_data in self._image_by_page.get(page["page"], []):
                self.chunks.append(self._build_image_chunk(page["page"], img_data))

        self._add_table_chunks()
        self._link_related_chunks()

        enriched = sum(
            1 for c in self.chunks
            if c.get("content_type") == "image_ocr"
        )
        placeholder = sum(
            1 for c in self.chunks
            if c.get("content_type") == "image_placeholder"
        )
        if enriched or placeholder:
            print(f"  Image chunks: {enriched} with OCR text, {placeholder} placeholder(s)")
        print(f"  Created {len(self.chunks)} semantic chunks")
        return self.chunks

    def _group_by_headings(self, page: Dict) -> List[Dict]:
        """Group page content under headings."""
        sections: List[Dict] = []
        current: Dict[str, Any] = {
            "heading": "Untitled",
            "level": 3,
            "content": [],
            "tables": [],
            "start_y": 0,
        }

        all_elements: List[tuple] = []

        for h in page.get("headings", []):
            all_elements.append(("heading", h))

        for b in page.get("text_blocks", []):
            all_elements.append(("text", b))

        all_elements.sort(key=lambda x: x[1].get("y_pos", 0))

        for elem_type, elem in all_elements:
            if elem_type == "heading":
                if current["content"] or current["tables"]:
                    sections.append(current.copy())

                current = {
                    "heading": elem["text"],
                    "level": elem.get("level", 3),
                    "content": [],
                    "tables": [],
                    "start_y": elem.get("y_pos", 0),
                }
            elif elem_type == "text":
                current["content"].append(elem["text"])

        if current["content"] or current["tables"]:
            sections.append(current)

        return sections

    def _build_chunk(
        self,
        section: Dict,
        page_num: int,
    ) -> Optional[Dict]:
        """Build a chunk from a section."""
        if not section["content"] and not section["tables"]:
            return None

        text_parts = []
        if section["heading"] != "Untitled":
            text_parts.append(
                f"{'#' * section['level']} {section['heading']}"
            )
        text_parts.extend(section["content"])

        section_tables = []
        for table in self.extraction.get("tables", []):
            if table.get("page") == page_num:
                section_tables.append(table)

        chunk_text = "\n\n".join(text_parts)

        if (
            len(chunk_text) < self.config.min_chunk_size
            and not section_tables
        ):
            return None

        has_tables = len(section_tables) > 0
        section_type = self._infer_section_type(section["heading"])
        preservation_level = self._infer_preservation_level(section_type, has_tables)

        chunk = {
            "chunk_id": f"chunk_{len(self.chunks):06d}",
            "page": page_num,
            "heading": section["heading"],
            "level": section["level"],
            "text": chunk_text,
            "tables": section_tables,
            "has_tables": has_tables,
            "char_count": len(chunk_text),
            "word_count": len(chunk_text.split()),
            "section_type": section_type,
            "preservation_level": preservation_level.value,
            # Populated during parent-child migration (future PR).
            "related_chunk_ids": [],
        }
        chunk["clinical_metadata"] = self._extract_clinical_metadata(chunk)
        return chunk

    def _add_table_chunks(self) -> None:
        """Add standalone chunks for important tables."""
        for table in self.extraction.get("tables", []):
            already_included = False
            for chunk in self.chunks:
                if table in chunk.get("tables", []):
                    already_included = True
                    break

            if not already_included and table.get("num_rows", 0) > 1:
                table_chunk = {
                    "chunk_id": f"chunk_table_{len(self.chunks):06d}",
                    "page": table.get("page", 0),
                    "heading": (
                        f"Table: {table.get('headers', ['Unknown'])[0] if table.get('headers') else 'Medical Table'}"
                    ),
                    "level": 3,
                    "text": f"## Dosing Table\n\n{table.get('markdown', '')}",
                    "tables": [table],
                    "has_tables": True,
                    "char_count": len(table.get("markdown", "")),
                    "word_count": len(table.get("markdown", "").split()),
                    "is_table_only": True,
                    "section_type": "table",
                    "preservation_level": PreservationLevel.VERBATIM.value,
                    "related_chunk_ids": [],
                }
                table_chunk["clinical_metadata"] = self._extract_clinical_metadata(table_chunk)
                self.chunks.append(table_chunk)

    def create_search_index(self) -> Dict:
        """Create BM25 search index from chunks."""
        print("\n🔍 Creating search index...")

        tokenized_chunks: List[List[str]] = []
        for chunk in self.chunks:
            text = chunk["text"]
            tokens = re.findall(r"[a-zA-Z0-9]+", text.lower())
            tokens = [t for t in tokens if len(t) > 1]
            tokenized_chunks.append(tokens)

            if chunk.get("tables"):
                for table in chunk["tables"]:
                    table_text = json.dumps(table.get("data", "")).lower()
                    table_tokens = re.findall(r"[a-zA-Z0-9]+", table_text)
                    table_tokens = [t for t in table_tokens if len(t) > 1]
                    tokenized_chunks[-1].extend(table_tokens)

        bm25 = BM25Okapi(tokenized_chunks)

        self.chunk_index = {
            "bm25": bm25,
            "chunks": self.chunks,
            "tokenized": tokenized_chunks,
        }

        return self.chunk_index
