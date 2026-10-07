# Cabling Map

## Purpose

This document defines the planned network and power connections for the rack-design lab.

---

## Network Cabling

| Cable ID | Source | Source Port | Destination | Destination Port | Purpose |
|---|---|---|---|---|---|
| SRV01-NIC1-SWA | Server 1 | NIC 1 | Switch A | Port 1 | Network Path A |
| SRV01-NIC2-SWB | Server 1 | NIC 2 | Switch B | Port 1 | Network Path B |
| SRV02-NIC1-SWA | Server 2 | NIC 1 | Switch A | Port 2 | Network Path A |
| SRV02-NIC2-SWB | Server 2 | NIC 2 | Switch B | Port 2 | Network Path B |
| SRV03-NIC1-SWA | Server 3 | NIC 1 | Switch A | Port 3 | Network Path A |
| SRV03-NIC2-SWB | Server 3 | NIC 2 | Switch B | Port 3 | Network Path B |
| PPA-SWA-UPLINK | Patch Panel A | Port 1 | Switch A | Uplink 1 | Upstream Path A |
| PPB-SWB-UPLINK | Patch Panel B | Port 1 | Switch B | Uplink 1 | Upstream Path B |

> Port numbers are illustrative and can be changed to match actual lab hardware.

---

## Power Cabling

| Cable ID | Source | Destination | Purpose |
|---|---|---|---|
| SRV01-PSU1-PDUA | Server 1 PSU 1 | PDU A | Power Path A |
| SRV01-PSU2-PDUB | Server 1 PSU 2 | PDU B | Power Path B |
| SRV02-PSU1-PDUA | Server 2 PSU 1 | PDU A | Power Path A |
| SRV02-PSU2-PDUB | Server 2 PSU 2 | PDU B | Power Path B |
| SRV03-PSU1-PDUA | Server 3 PSU 1 | PDU A | Power Path A |
| SRV03-PSU2-PDUB | Server 3 PSU 2 | PDU B | Power Path B |

---

## Labeling Standard

### Network

```text
SRV##-NIC#-SW#
```

Examples:

```text
SRV01-NIC1-SWA
SRV01-NIC2-SWB
SRV02-NIC1-SWA
SRV02-NIC2-SWB
```

### Power

```text
SRV##-PSU#-PDU#
```

Examples:

```text
SRV01-PSU1-PDUA
SRV01-PSU2-PDUB
```

---

## Cable Management Notes

- Keep network and power cabling organized and separated where practical.
- Avoid blocking server airflow.
- Use Velcro-style reusable cable ties rather than overtightened plastic ties where possible.
- Maintain bend-radius requirements for fiber cabling.
- Label both ends of every cable.
- Do not route both redundant paths through the same avoidable physical failure point when diversity is required.
- Document any port or cable changes immediately.
