#!/usr/bin/env python3
"""Validate a homelab hardware asset register (CSV), using Python stdlib only."""
from __future__ import annotations
import argparse
import csv
import ipaddress
from datetime import date
from pathlib import Path
import sys

REQUIRED_HEADERS = [
    "Asset ID", "Hostname", "Type", "Vendor / Model", "Serial Number",
    "Rack", "Start U", "Height U", "CPU", "RAM (GB)", "Storage",
    "NIC / Ports", "Mgmt Interface", "Mgmt IP", "Firmware / BIOS",
    "OS / Hypervisor", "Status", "Owner", "Last Verified", "Environment", "Notes",
]
STATUSES = {"In Service", "Maintenance", "Spare", "Retired"}
REQUIRED_VALUES = ("Asset ID", "Hostname", "Type", "Vendor / Model", "Serial Number", "Status", "Last Verified")


def validate_file(path: str | Path) -> tuple[list[str], int]:
    errors: list[str] = []
    with open(path, newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        headers = reader.fieldnames or []
        missing = [name for name in REQUIRED_HEADERS if name not in headers]
        if missing:
            return (["Missing required columns: " + ", ".join(missing)], 0)
        rows = list(reader)

    seen_ids: dict[str, int] = {}
    seen_serials: dict[str, int] = {}
    seen_ips: dict[str, int] = {}
    occupied: dict[tuple[str, int], tuple[str, int]] = {}
    count = 0

    for line_num, record in enumerate(rows, start=2):
        row = {k: (record.get(k) or "").strip() for k in REQUIRED_HEADERS}
        if not any(row.values()):
            continue
        count += 1
        for field in REQUIRED_VALUES:
            if not row[field]:
                errors.append(f"Row {line_num}: missing {field}")

        for field, seen in (("Asset ID", seen_ids), ("Serial Number", seen_serials), ("Mgmt IP", seen_ips)):
            val = row[field]
            if val and val.upper() not in {"N/A", "TBD", "UNKNOWN"}:
                if val in seen:
                    errors.append(f"Row {line_num}: duplicate {field} {val!r} (first row {seen[val]})")
                else:
                    seen[val] = line_num

        if row["Status"] and row["Status"] not in STATUSES:
            errors.append(f"Row {line_num}: unsupported status {row['Status']!r}; allowed: {', '.join(sorted(STATUSES))}")
        if row["Mgmt IP"]:
            try:
                ipaddress.ip_address(row["Mgmt IP"])
            except ValueError:
                errors.append(f"Row {line_num}: invalid management IP {row['Mgmt IP']!r}")
        if row["Last Verified"]:
            try:
                date.fromisoformat(row["Last Verified"])
            except ValueError:
                errors.append(f"Row {line_num}: Last Verified must be YYYY-MM-DD")
        if row["RAM (GB)"] not in {"", "N/A"}:
            try:
                if float(row["RAM (GB)"]) < 0:
                    raise ValueError
            except ValueError:
                errors.append(f"Row {line_num}: RAM (GB) must be a non-negative number or N/A")
        rack, start_text, height_text = row["Rack"], row["Start U"], row["Height U"]
        if any((rack, start_text, height_text)):
            if not all((rack, start_text, height_text)):
                errors.append(f"Row {line_num}: Rack, Start U, and Height U must be set together")
            else:
                try:
                    start, height = int(start_text), int(height_text)
                    if not (1 <= start <= 42 and 1 <= height <= 42 and start + height - 1 <= 42):
                        raise ValueError
                except ValueError:
                    errors.append(f"Row {line_num}: rack units must be integers within a 42U rack")
                else:
                    for unit in range(start, start + height):
                        key = (rack.casefold(), unit)
                        if key in occupied:
                            other_id, other_line = occupied[key]
                            errors.append(f"Row {line_num}: {rack} U{unit} overlaps {other_id} (row {other_line})")
                        else:
                            occupied[key] = (row["Asset ID"], line_num)
        if row["Status"] in {"In Service", "Maintenance"} and not row["Firmware / BIOS"]:
            errors.append(f"Row {line_num}: firmware record required for an active asset")

    return errors, count


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a homelab asset register CSV")
    parser.add_argument("csv_file", type=Path, help="Path to inventory CSV")
    args = parser.parse_args()
    try:
        issues, count = validate_file(args.csv_file)
    except (OSError, UnicodeError, csv.Error) as exc:
        print(f"ERROR: cannot read CSV: {exc}", file=sys.stderr)
        return 2
    if issues:
        for issue in issues:
            print("ERROR:", issue, file=sys.stderr)
        print(f"FAIL: {count} assets; {len(issues)} issue(s)", file=sys.stderr)
        return 1
    print(f"PASS: {count} assets validated; no duplicate IDs/serials/IPs or rack overlaps")
    return 0


if __name__ == "__main__":
    sys.exit(main())
