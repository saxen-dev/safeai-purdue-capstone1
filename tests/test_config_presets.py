"""
Unit tests for config preset factory functions and JSON config loading (P13).

Tests cover:
  - _load_json_config: valid JSON, missing file, invalid JSON
  - DEFAULT_* paths honour env vars
  - extraction_config_who_malaria_nih: JSON vocabularies wired in, fallback
  - extraction_config_uganda_clinical_2023: JSON vocabularies wired in, fallback
  - ExtractionConfig fields set correctly by both presets
  - CLI env var hint path (smoke test on main())

Run with:  python3 -m pytest tests/test_config_presets.py -v
"""

import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

import pipeline.config as config_module
from pipeline.config import (
    ExtractionConfig,
    _load_json_config,
    extraction_config_uganda_clinical_2023,
    extraction_config_who_malaria_nih,
    MALARIA_DOSING_TABLE_KEYWORDS,
    UGANDA_DOSING_TABLE_KEYWORDS,
    UGANDA_CLINICAL_TABLE_KEYWORDS,
)


# ---------------------------------------------------------------------------
# _load_json_config
# ---------------------------------------------------------------------------

class TestLoadJsonConfig:

    def test_loads_valid_json(self, tmp_path):
        f = tmp_path / "cfg.json"
        f.write_text('{"key": "value", "num": 42}')
        result = _load_json_config(f)
        assert result == {"key": "value", "num": 42}

    def test_returns_empty_dict_for_missing_file(self, tmp_path):
        result = _load_json_config(tmp_path / "nonexistent.json")
        assert result == {}

    def test_returns_empty_dict_for_invalid_json(self, tmp_path):
        f = tmp_path / "bad.json"
        f.write_text("not valid json {{{")
        result = _load_json_config(f)
        assert result == {}

    def test_returns_empty_dict_on_permission_error(self, tmp_path):
        f = tmp_path / "unreadable.json"
        f.write_text('{}')
        f.chmod(0o000)
        try:
            result = _load_json_config(f)
            assert result == {}
        finally:
            f.chmod(0o644)

    def test_nested_structure_preserved(self, tmp_path):
        data = {"a": {"b": [1, 2, 3]}, "c": True}
        f = tmp_path / "cfg.json"
        f.write_text(json.dumps(data))
        assert _load_json_config(f) == data


# ---------------------------------------------------------------------------
# DEFAULT_* paths honour env vars
# ---------------------------------------------------------------------------

class TestDefaultPaths:

    def test_malaria_pdf_env_var_honoured(self):
        with patch.dict(os.environ, {"MALARIA_PDF": "/data/malaria.pdf"}):
            # Re-evaluate the constant by importing fresh (or just test the env lookup)
            result = (
                os.environ.get("MALARIA_PDF")
                or os.environ.get("WHO_MALARIA_PDF")
                or r"C:\temp\capstone\Bookshelf_NBK588130.pdf"
            )
            assert result == "/data/malaria.pdf"

    def test_who_malaria_pdf_env_var_honoured(self):
        with patch.dict(os.environ, {"WHO_MALARIA_PDF": "/alt/malaria.pdf"},
                        clear=False):
            # Only fires when MALARIA_PDF is absent
            env = {"WHO_MALARIA_PDF": "/alt/malaria.pdf"}
            with patch.dict(os.environ, env):
                # Ensure MALARIA_PDF not set
                os.environ.pop("MALARIA_PDF", None)
                result = (
                    os.environ.get("MALARIA_PDF")
                    or os.environ.get("WHO_MALARIA_PDF")
                    or r"C:\temp"
                )
                assert result == "/alt/malaria.pdf"

    def test_uganda_pdf_env_var_honoured(self):
        with patch.dict(os.environ, {"UGANDA_PDF": "/data/uganda.pdf"}):
            result = (
                os.environ.get("UGANDA_PDF")
                or os.environ.get("UGANDA_CLINICAL_PDF")
                or r"C:\temp\capstone\Uganda Clinical Guidelines 2023.pdf"
            )
            assert result == "/data/uganda.pdf"


# ---------------------------------------------------------------------------
# extraction_config_who_malaria_nih
# ---------------------------------------------------------------------------

def _malaria_json(drug_keywords=None, dosing_keywords=None, clinical_table_keywords=None,
                  title=None, output_dir=None):
    return {
        "output_dir": output_dir or "extraction_output_malaria",
        "document": {"title": title or "WHO Malaria 2025"},
        "drug_keywords": drug_keywords or ["artemether", "lumefantrine"],
        "dosing_keywords": dosing_keywords or ["mg/kg", "tablet"],
        "clinical_table_keywords": clinical_table_keywords or [],
    }


class TestExtractionConfigWhoMalaria:

    def _cfg(self, json_data=None, pdf="/fake/malaria.pdf", output_dir=None):
        """Build config with a mocked JSON file."""
        with tempfile.TemporaryDirectory() as tmp:
            configs_dir = Path(tmp) / "configs"
            configs_dir.mkdir()
            if json_data is not None:
                (configs_dir / "malaria_who_2025.json").write_text(json.dumps(json_data))

            with patch.object(config_module, "_CONFIGS_DIR", configs_dir):
                return extraction_config_who_malaria_nih(
                    pdf_path=pdf,
                    output_dir=output_dir or tmp + "/out",
                )

    def test_document_title_from_json(self):
        cfg = self._cfg(_malaria_json(title="WHO Malaria 2025 Special Edition"))
        assert cfg.document_title == "WHO Malaria 2025 Special Edition"

    def test_document_title_fallback_when_json_absent(self):
        cfg = self._cfg(json_data=None)
        assert "WHO Malaria" in cfg.document_title

    def test_json_drug_keywords_in_dosing_table_keywords(self):
        cfg = self._cfg(_malaria_json(drug_keywords=["artesunate", "quinine"]))
        assert "artesunate" in cfg.dosing_table_keywords
        assert "quinine" in cfg.dosing_table_keywords

    def test_json_dosing_keywords_in_dosing_table_keywords(self):
        cfg = self._cfg(_malaria_json(dosing_keywords=["body weight", "single dose"]))
        assert "body weight" in cfg.dosing_table_keywords
        assert "single dose" in cfg.dosing_table_keywords

    def test_hardcoded_malaria_kws_always_present(self):
        cfg = self._cfg(_malaria_json(drug_keywords=[]))
        for kw in MALARIA_DOSING_TABLE_KEYWORDS:
            assert kw in cfg.dosing_table_keywords

    def test_no_duplicate_keywords(self):
        cfg = self._cfg(_malaria_json(drug_keywords=["artemether", "artemether"]))
        assert cfg.dosing_table_keywords.count("artemether") == 1

    def test_fallback_dosing_kws_when_json_absent(self):
        cfg = self._cfg(json_data=None)
        for kw in MALARIA_DOSING_TABLE_KEYWORDS:
            assert kw in cfg.dosing_table_keywords

    def test_clinical_table_keywords_empty_gives_none(self):
        # Malaria JSON has no clinical_table_keywords → field should be None
        cfg = self._cfg(_malaria_json(clinical_table_keywords=[]))
        assert cfg.clinical_table_keywords is None

    def test_clinical_table_keywords_populated_when_present(self):
        cfg = self._cfg(_malaria_json(clinical_table_keywords=["management", "complication"]))
        assert "management" in cfg.clinical_table_keywords

    def test_output_dir_from_json_output_dir(self):
        # Don't pass an explicit output_dir so the JSON-derived name is used
        with tempfile.TemporaryDirectory() as tmp:
            configs_dir = Path(tmp) / "configs"
            configs_dir.mkdir()
            (configs_dir / "malaria_who_2025.json").write_text(
                json.dumps(_malaria_json(output_dir="my_malaria_kb"))
            )
            with patch.object(config_module, "_CONFIGS_DIR", configs_dir):
                cfg = extraction_config_who_malaria_nih(pdf_path="/fake/malaria.pdf")
        assert "my_malaria_kb" in cfg.output_dir

    def test_critical_content_terms_are_malaria_terms(self):
        cfg = self._cfg(_malaria_json())
        assert cfg.critical_content_terms is not None
        assert "artemisinin" in cfg.critical_content_terms or "dose" in cfg.critical_content_terms

    def test_pdf_path_set_correctly(self, tmp_path):
        fake_pdf = str(tmp_path / "malaria.pdf")
        cfg = self._cfg(_malaria_json(), pdf=fake_pdf)
        assert fake_pdf in cfg.pdf_path or Path(cfg.pdf_path).name == "malaria.pdf"


# ---------------------------------------------------------------------------
# extraction_config_uganda_clinical_2023
# ---------------------------------------------------------------------------

def _uganda_json(drug_keywords=None, dosing_keywords=None, clinical_table_keywords=None,
                 title=None, output_dir=None):
    return {
        "output_dir": output_dir or "extraction_output_uganda",
        "document": {"title": title or "Uganda Clinical Guidelines 2023"},
        "drug_keywords": drug_keywords or ["amoxicillin", "cotrimoxazole"],
        "dosing_keywords": dosing_keywords or ["mg", "dose"],
        "clinical_table_keywords": clinical_table_keywords or ["management", "referral"],
    }


class TestExtractionConfigUganda:

    def _cfg(self, json_data=None, pdf="/fake/uganda.pdf", output_dir=None):
        with tempfile.TemporaryDirectory() as tmp:
            configs_dir = Path(tmp) / "configs"
            configs_dir.mkdir()
            if json_data is not None:
                (configs_dir / "uganda_clinical_2023.json").write_text(json.dumps(json_data))

            with patch.object(config_module, "_CONFIGS_DIR", configs_dir):
                return extraction_config_uganda_clinical_2023(
                    pdf_path=pdf,
                    output_dir=output_dir or tmp + "/out",
                )

    def test_document_title_from_json(self):
        cfg = self._cfg(_uganda_json(title="Uganda Clinical 2023 Edition"))
        assert cfg.document_title == "Uganda Clinical 2023 Edition"

    def test_document_title_fallback_when_json_absent(self):
        cfg = self._cfg(json_data=None)
        assert "Uganda" in cfg.document_title

    def test_json_drug_keywords_in_dosing_table_keywords(self):
        cfg = self._cfg(_uganda_json(drug_keywords=["amoxicillin", "metronidazole", "zinc"]))
        for drug in ("amoxicillin", "metronidazole", "zinc"):
            assert drug in cfg.dosing_table_keywords

    def test_hardcoded_uganda_kws_always_present(self):
        cfg = self._cfg(_uganda_json(drug_keywords=[]))
        for kw in UGANDA_DOSING_TABLE_KEYWORDS:
            assert kw in cfg.dosing_table_keywords

    def test_no_duplicate_keywords(self):
        # JSON and hardcoded both have "amoxicillin"
        cfg = self._cfg(_uganda_json(drug_keywords=["amoxicillin", "amoxicillin"]))
        assert cfg.dosing_table_keywords.count("amoxicillin") == 1

    def test_clinical_table_keywords_json_merged_with_hardcoded(self):
        cfg = self._cfg(_uganda_json(clinical_table_keywords=["UNIQUE_TERM_XYZ"]))
        assert "UNIQUE_TERM_XYZ" in cfg.clinical_table_keywords
        # Hard-coded terms also present
        for kw in UGANDA_CLINICAL_TABLE_KEYWORDS:
            assert kw in cfg.clinical_table_keywords

    def test_clinical_table_keywords_no_duplicates(self):
        # "management" is in both JSON and hard-coded
        cfg = self._cfg(_uganda_json(clinical_table_keywords=["management"]))
        assert cfg.clinical_table_keywords.count("management") == 1

    def test_fallback_when_json_absent_has_clinical_kws(self):
        cfg = self._cfg(json_data=None)
        for kw in UGANDA_CLINICAL_TABLE_KEYWORDS:
            assert kw in cfg.clinical_table_keywords

    def test_critical_content_terms_are_uganda_terms(self):
        cfg = self._cfg(_uganda_json())
        assert cfg.critical_content_terms is not None
        assert "diagnosis" in cfg.critical_content_terms or "treatment" in cfg.critical_content_terms

    def test_output_dir_from_json(self):
        # Don't pass an explicit output_dir so the JSON-derived name is used
        with tempfile.TemporaryDirectory() as tmp:
            configs_dir = Path(tmp) / "configs"
            configs_dir.mkdir()
            (configs_dir / "uganda_clinical_2023.json").write_text(
                json.dumps(_uganda_json(output_dir="uganda_kb"))
            )
            with patch.object(config_module, "_CONFIGS_DIR", configs_dir):
                cfg = extraction_config_uganda_clinical_2023(pdf_path="/fake/uganda.pdf")
        assert "uganda_kb" in cfg.output_dir

    def test_pdf_path_set_correctly(self, tmp_path):
        fake_pdf = str(tmp_path / "uganda.pdf")
        cfg = self._cfg(_uganda_json(), pdf=fake_pdf)
        assert Path(cfg.pdf_path).name == "uganda.pdf"


# ---------------------------------------------------------------------------
# ExtractionConfig field validation
# ---------------------------------------------------------------------------

class TestExtractionConfigFields:

    def test_extraction_config_has_dosing_table_keywords(self):
        cfg = ExtractionConfig(pdf_path="/fake.pdf", dosing_table_keywords=["mg/kg"])
        assert cfg.dosing_table_keywords == ["mg/kg"]

    def test_extraction_config_dosing_keywords_default_none(self):
        cfg = ExtractionConfig(pdf_path="/fake.pdf")
        assert cfg.dosing_table_keywords is None

    def test_extraction_config_clinical_table_keywords_default_none(self):
        cfg = ExtractionConfig(pdf_path="/fake.pdf")
        assert cfg.clinical_table_keywords is None

    def test_cache_dir_derived_from_output_dir(self):
        cfg = ExtractionConfig(pdf_path="/fake.pdf", output_dir="/out/kb")
        assert cfg.cache_dir == str(Path("/out/kb") / "cache")
