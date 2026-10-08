# Homelab Hardware Asset Inventory

**Portfolio status:** ✅ Asset inventory completed — **demonstration dataset**  
**Focus:** Data-center operations · rack documentation · hardware lifecycle · firmware tracking · data quality

A GitHub portfolio project demonstrating how to document and verify a small homelab's hardware estate. The asset register captures **serial number, rack/U position, CPU, RAM, storage, network interfaces, management IP, installed firmware, and operational status**, along with owner and verification date.

> **Dataset disclaimer:** The seven devices in `data/sample_inventory.csv` are **synthetic examples**, not actual discovered hardware. `DEMO-SN-*` serials and the RFC 5737 `192.0.2.0/24` documentation addresses are used intentionally. Do **not** describe the example data as a verified physical inventory.

## Project outcomes

- [x] Designed a standardized asset register with 21 fields covering physical, compute, network, management, and lifecycle details.
- [x] Documented seven **sample** homelab assets in one consistent CSV and Excel format.
- [x] Documented rack positions and 2U/1U device occupancy with overlap detection.
- [x] Added automated checks for duplicate asset IDs, serials, management IPs, invalid IPs, inconsistent rack positions, status values, and date formats.
- [x] Added unit tests and GitHub Actions validation to keep inventory changes consistent.
- [x] Created a data dictionary and a collection / re-verification SOP.

## Example inventory snapshot

| Asset ID | Device | Rack/U | CPU / memory | Storage | NIC | Mgmt IP | Firmware | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AS-001 | compute-01 | Rack-A U04–U05 | 2× Xeon Silver 4210 / 128 GB | 2×480 GB SSD + 4×2 TB HDD | 2×10 GbE + 2×1 GbE | 192.0.2.11 | DEMO BIOS/iDRAC | In Service |
| AS-002 | compute-02 | Rack-A U07–U08 | 2× Xeon Silver 4110 / 96 GB | 2×960 GB SSD | 4×1 GbE | 192.0.2.12 | DEMO BIOS/iLO | Maintenance |
| AS-003 | storage-01 | Rack-A U10–U11 | Ryzen V1500B / 32 GB | 4×8 TB HDD + 2×1 TB SSD | 4×1 GbE | 192.0.2.13 | DEMO DSM | In Service |
| AS-004 | switch-01 | Rack-A U02 | Embedded / 2 GB | N/A | 24×1 GbE + 2×10 GbE | 192.0.2.14 | DEMO Switch OS | In Service |
| AS-005 | firewall-01 | Rack-A U01 | Atom C3558 / 8 GB | 128 GB SSD | 2×10 GbE + 4×2.5 GbE | 192.0.2.15 | DEMO pfSense | In Service |
| AS-006 | ups-01 | Rack-A U14–U15 | N/A | N/A | Mgmt Ethernet | 192.0.2.16 | DEMO NMC | In Service |
| AS-007 | spare-01 | Not racked | Xeon Silver 4114 / 32 GB | 2×480 GB SSD | 2×1 GbE | Unassigned | DEMO BIOS | Spare |

Full fields, including **serial number**, are in `data/sample_inventory.csv` and `Homelab_Asset_Inventory.xlsx`.

## Files

```text
homelab-asset-inventory/
├── README.md
├── Homelab_Asset_Inventory.xlsx   # Excel dashboard + asset register + field guide
├── data/
│   ├── sample_inventory.csv       # Synthetic, GitHub-safe records
│   └── inventory_template.csv     # Blank CSV for a new inventory
├── docs/
│   └── DATA_DICTIONARY.md         # Field definitions and collection SOP
├── scripts/
│   └── validate_inventory.py      # Stdlib-only QA: IDs, IPs, dates, rack/U
├── tests/
│   └── test_validate_inventory.py
└── .github/workflows/
    └── validate.yml              # CI runs validator + unit tests
```

## Run validation

Python 3.11+; no external dependencies required for CLI validation.

```bash
python scripts/validate_inventory.py data/sample_inventory.csv
# PASS: 7 assets validated; no duplicate IDs/serials/IPs or rack overlaps

python -m unittest discover -s tests -v
```

## Use it in your own homelab

1. Copy `data/inventory_template.csv` into a **private** workspace; add **measured** asset data.
2. Record rack occupancy using bottom-up U numbering, and enter the installed BIOS/firmware version.
3. Validate exported CSV with the script, correct issues, and date the verification.
4. Update the Excel sheet for filters, KPI totals, and review workflows; its demo data is a starting example, not automatically synchronized with CSV.
5. Publish only sanitized data and screenshots with identifying details removed.

See [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md) for the field guide and data collection procedure.

## What this demonstrates to employers

**Data Center Operations / AWS DCO aligned skills:** asset identification and lifecycle tracking, rack-space awareness, documenting compute/storage/network hardware, management-plane awareness, installed firmware visibility, operational-status reporting, and repeatable quality checks. This project documents process skills; it does **not** claim work performed on AWS production systems.

### Resume / portfolio entry

> **Homelab Hardware Asset Inventory — Completed (Demo Project)**  
> Designed a 21-field hardware register for seven simulated lab assets, capturing rack/U occupancy, serials, CPU, RAM, storage, NICs, management endpoints, firmware, and lifecycle status. Implemented automated inventory integrity checks, Python unit tests, and GitHub Actions validation.

## Security and privacy

The source CSV intentionally uses placeholder serials and non-routable documentation IPs. Do not commit real hardware serials, reachable management IPs, BMC login details, credentials, public-facing access URLs, or unredacted config exports to a public repo.

---
**License:** This example is provided for portfolio and educational reuse; customize the attribution and license before public distribution.
