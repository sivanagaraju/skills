#!/usr/bin/env python3
"""
test_validate_package.py — Automated Unit Test Suite for validate_package.py
Tests the 7-pillar package architecture, references.md, MathsTerms link validation,
curriculum bridge verification, and Python example script execution.
"""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from validate_package import (
    Report,
    check_references_md,
    check_notes_references_delegation,
    check_relative_links,
    check_examples_scripts,
    check_glossary_md,
    check_formulae_sheet_md,
    scan_derivation_gaps,
)


class TestValidatePackage(unittest.TestCase):
    def setUp(self) -> None:
        self.test_dir = Path(tempfile.mkdtemp())
        self.rep = Report()

    def tearDown(self) -> None:
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_references_md_valid(self) -> None:
        ref_file = self.test_dir / "references.md"
        ref_file.write_text(
            "# References\n\n"
            "## 1. Curriculum & Prerequisite Bridges\n"
            "- [Lec 07: IID](../../Mathematical-foundation-ml/08-Lec07-IID-Assumption/NOTES.md)\n\n"
            "## 2. Foundational & Seminal Papers\n"
            "- [Goodfellow 2014](https://arxiv.org/abs/1406.2661)\n\n"
            "## 3. Authoritative Textbooks & Video Lectures\n"
            "- Murphy PML Chapter 20\n\n"
            "## 4. Industry Implementation Guides\n"
            "- [PyTorch](https://pytorch.org)\n\n"
            "## 5. Interactive Visualizers\n"
            "- [Visualizer](https://distill.pub)\n",
            encoding="utf-8",
        )
        check_references_md(self.test_dir, self.rep, {"package_status": "current"})
        self.assertEqual(len(self.rep.errors), 0)

    def test_references_md_missing_current(self) -> None:
        check_references_md(self.test_dir, self.rep, {"package_status": "current"})
        self.assertTrue(any("missing mandatory 7th pillar references.md" in e for e in self.rep.errors))

    def test_references_md_missing_legacy(self) -> None:
        check_references_md(self.test_dir, self.rep, {"package_status": "legacy"})
        self.assertEqual(len(self.rep.errors), 0)
        self.assertTrue(any("legacy package" in w for w in self.rep.warns))

    def test_notes_references_delegation(self) -> None:
        notes_file = self.test_dir / "NOTES.md"
        notes_file.write_text(
            "# Notes\n\n"
            "## References & Further Reading\n"
            "For full annotated citations, see [references.md](./references.md).\n",
            encoding="utf-8",
        )
        check_notes_references_delegation(notes_file, self.rep)
        self.assertEqual(len(self.rep.errors), 0)
        self.assertEqual(len(self.rep.warns), 0)

    def test_notes_missing_references_delegation_warns(self) -> None:
        notes_file = self.test_dir / "NOTES.md"
        notes_file.write_text("# Notes\n\nJust content without reference pointer.\n", encoding="utf-8")
        check_notes_references_delegation(notes_file, self.rep)
        self.assertTrue(any("references.md" in w for w in self.rep.warns))

    def test_relative_links_mathsterms(self) -> None:
        # Create fake MathsTerms target
        target_dir = self.test_dir / "MathsTerms" / "03-Calculus"
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / "06-Softmax.md"
        target_file.write_text("# Softmax\n", encoding="utf-8")

        # Create package dir
        pkg_dir = self.test_dir / "packages" / "Lec01"
        pkg_dir.mkdir(parents=True, exist_ok=True)
        notes = pkg_dir / "NOTES.md"
        notes.write_text(
            "See [Softmax](../../MathsTerms/03-Calculus/06-Softmax.md) and [Broken](../../MathsTerms/03-Calculus/Broken.md).\n",
            encoding="utf-8",
        )

        check_relative_links(pkg_dir, self.rep)
        self.assertTrue(any("Broken.md" in e for e in self.rep.errors))
        self.assertFalse(any("06-Softmax.md" in e for e in self.rep.errors))

    def test_relative_links_curriculum_bridge(self) -> None:
        # Create fake Mathematical-foundation-ml target
        ml_dir = self.test_dir / "Mathematical-foundation-ml" / "08-Lec07-IID-Assumption"
        ml_dir.mkdir(parents=True, exist_ok=True)
        (ml_dir / "NOTES.md").write_text("# IID\n", encoding="utf-8")

        # Create package dir
        pkg_dir = self.test_dir / "packages" / "Lec01"
        pkg_dir.mkdir(parents=True, exist_ok=True)
        prereqs = pkg_dir / "PREREQUISITES.md"
        prereqs.write_text(
            "See [IID](../../Mathematical-foundation-ml/08-Lec07-IID-Assumption/NOTES.md) and "
            "[Broken](../../Mathematical-foundation-ml/99-NonExistent/NOTES.md).\n",
            encoding="utf-8",
        )

        check_relative_links(pkg_dir, self.rep)
        self.assertTrue(any("99-NonExistent" in e for e in self.rep.errors))
        self.assertFalse(any("08-Lec07-IID-Assumption" in e for e in self.rep.errors))

    def test_examples_execution_pass(self) -> None:
        examples_dir = self.test_dir / "examples"
        examples_dir.mkdir()
        script = examples_dir / "01_test.py"
        script.write_text("x = 10 + 20\nassert x == 30\nprint('Pass')\n", encoding="utf-8")

        check_examples_scripts(self.test_dir, self.rep, {"package_status": "current"}, skip_exec=False)
        self.assertEqual(len(self.rep.errors), 0)

    def test_examples_execution_fail(self) -> None:
        examples_dir = self.test_dir / "examples"
        examples_dir.mkdir()
        script = examples_dir / "01_fail.py"
        script.write_text("assert False, 'Deliberate test failure'\n", encoding="utf-8")

        check_examples_scripts(self.test_dir, self.rep, {"package_status": "current"}, skip_exec=False)
        self.assertTrue(any("execution failed" in e for e in self.rep.errors))

    def test_glossary_validation(self) -> None:
        glossary = self.test_dir / "glossary.md"
        glossary.write_text(
            "# Glossary\n\n"
            "| Term / Notation | Formal Definition | Plain-English Software Meaning | Spoken English (Phonetics) |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| $\\nabla f$ | Gradient | Direction of steepest ascent | DEL EFF |\n",
            encoding="utf-8",
        )
        check_glossary_md(self.test_dir, self.rep, {"package_status": "current"})
        self.assertEqual(len(self.rep.errors), 0)

    def test_formulae_sheet_validation(self) -> None:
        sheet = self.test_dir / "formulae_sheet.md"
        sheet.write_text(
            "# Formulae Sheet\n\n"
            "## 1. Master Equations Index\n$$\\nabla f$$\n\n"
            "## 2. Input/Output Tensor Dimensionality\nShapes\n\n"
            "## 3. Mathematical Guarantees & Invariants\nProperties\n\n"
            "## 4. Contrastive Decision Table\nWhy X Not Y\n",
            encoding="utf-8",
        )
        check_formulae_sheet_md(self.test_dir, self.rep, {"package_status": "current"})
        self.assertEqual(len(self.rep.errors), 0)

    def test_derivation_gap_detection(self) -> None:
        text = "From equation 1, it can easily be seen that x = y, and obviously the gradient vanishes."
        scan_derivation_gaps(text, "TEST.md", self.rep)
        self.assertTrue(any("it can easily be seen that" in w for w in self.rep.warns))
        self.assertTrue(any("obviously" in w for w in self.rep.warns))


if __name__ == "__main__":
    unittest.main()
