"""Unit tests for the homelab asset inventory validator."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_inventory import validate_file  # noqa: E402


class InventoryValidationTests(unittest.TestCase):
    def setUp(self):
        with (ROOT / "data" / "sample_inventory.csv").open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.fields = reader.fieldnames
            self.rows = list(reader)

    def check_modified(self, change):
        rows = [dict(row) for row in self.rows]
        change(rows)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "test.csv"
            with path.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=self.fields)
                writer.writeheader()
                writer.writerows(rows)
            return validate_file(path)[0]

    def test_sample_passes(self):
        errors, count = validate_file(ROOT / "data" / "sample_inventory.csv")
        self.assertEqual(count, 7)
        self.assertEqual(errors, [])

    def test_duplicate_serial_flagged(self):
        errors = self.check_modified(lambda rows: rows[1].update({"Serial Number": rows[0]["Serial Number"]}))
        self.assertTrue(any("duplicate Serial Number" in e for e in errors))

    def test_rack_overlap_flagged(self):
        errors = self.check_modified(lambda rows: rows[1].update({"Start U": "5"}))
        self.assertTrue(any("overlaps" in e for e in errors))

    def test_invalid_ip_flagged(self):
        errors = self.check_modified(lambda rows: rows[0].update({"Mgmt IP": "999.999.999.999"}))
        self.assertTrue(any("invalid management IP" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
