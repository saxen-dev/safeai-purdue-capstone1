"""
Smart chunking: semantic chunks from extracted content with BM25 index.
"""

import json
import re
from typing import Dict, List, Optional, Any

from rank_bm25 import BM25Okapi

from .config import ExtractionConfig, PreservationLevel

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
        self.chunk_index: Dict[str, Any] = {}

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

    def chunk_by_headings(self) -> List[Dict]:
        """Create chunks based on document headings."""
        print("\n🧩 Creating semantic chunks...")

        for page in self.extraction.get("pages", []):
            sections = self._group_by_headings(page)

            for section in sections:
                chunk = self._build_chunk(section, page["page"])
                if chunk:
                    self.chunks.append(chunk)

        self._add_table_chunks()

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

        return {
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
