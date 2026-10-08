# Asset register field guide

| Field | Requirement / meaning |
| --- | --- |
| Asset ID | Unique stable identifier; never reused. |
| Hostname | DNS / management label for device. |
| Type | Server, NAS, Switch, Firewall, UPS, or another device type. |
| Vendor / Model | Physical vendor and manufacturer model. |
| Serial Number | Serial from device label, BIOS/UEFI, iDRAC/iLO, or CLI. Do **not** publish actual serials in public repos. |
| Rack | Rack name, e.g. `Rack-A`; blank if off-rack. |
| Start U | Lowest occupied rack unit (assumes bottom-up U numbering). |
| Height U | Vertical height occupied; leave blank when not racked. |
| CPU | Model and quantity or `N/A`. |
| RAM (GB) | Total installed capacity in GB or `N/A`. |
| Storage | Drive sizes, counts, interface, and RAID/ZFS/SHR layout, as applicable. |
| NIC / Ports | Port counts, speeds, and interface types. |
| Mgmt Interface | iDRAC, iLO, IPMI, web UI, SSH, NMC, etc. |
| Mgmt IP | Unique IP address of management plane; blank if unassigned. Do **not** publish reachable private addresses. |
| Firmware / BIOS | Currently installed version(s) as read from hardware, not merely latest available online. |
| OS / Hypervisor | Host OS, hypervisor, or embedded OS. |
| Status | `In Service`, `Maintenance`, `Spare`, `Retired`. |
| Owner | Person or team accountable for updates. |
| Last Verified | Date physically or remotely confirmed; ISO format `YYYY-MM-DD`. |
| Environment | Lab, Test, Production, etc. |
| Notes | Exceptions, location details, lifecycle actions, or outstanding verification. |

## Inventory collection procedure

1. Create and label a stable asset ID; photograph/record the model tag **privately**.
2. Document `rack`, `Start U`, and `Height U` by looking at the rack; check no other asset uses those units.
3. Gather CPU, RAM, storage, and NIC information using device console or manufacturer tools.
4. Record the dedicated management interface and management IP; never add credentials.
5. Record **installed** BIOS/firmware versions; record verification date and service status.
6. Enter real data in a **private** register. Only commit anonymized data to the public GitHub project.
7. Export CSV and run `python scripts/validate_inventory.py path/to/inventory.csv`.
8. Review and reverify after hardware moves, component changes, firmware updates, and quarterly audits.

## Useful read-only discovery examples

Linux: `sudo dmidecode -t system -t processor -t memory`, `lsblk -o NAME,SIZE,MODEL,TYPE`, `ip -br link`, `sudo ethtool <interface>`.

Proxmox: `pveversion -v`, `lscpu`, `free -h`, `lsblk`, `ip -br a`.

Network devices / BMC: read serial and firmware from manufacturer management UI, `show version`, or supported Redfish endpoints. Do not commit BMC/API responses containing serials, MACs, tokens, or management addresses.

> **Important:** All committed demo serial numbers begin `DEMO-` and all example management IPs are from `192.0.2.0/24` (documentation-only range). Vendor/model/spec combinations are illustrative, not attestations of real devices.
