# One-Page Hardware Inspection Checklist

**Date:** __________  **Device ID (non-sensitive alias):** __________  **Inspector:** __________  
**Environment:** [ ] Physical PC  [ ] VM guest  **OS:** __________  **Hypervisor (if VM):** __________

## 1. Firmware / physical or virtual hardware

- [ ] Confirmed device is authorized for inspection; documented PC vs VM guest.
- [ ] Opened BIOS/UEFI System Information or reviewed VM firmware/hardware settings.
- [ ] Recorded manufacturer/model or VM platform: ______________________________
- [ ] Recorded CPU model / vCPU allocation: ____________________________________
- [ ] Recorded installed/allocated RAM: __________ GB or GiB (circle unit)
- [ ] Recorded detected disk(s) and sizes: ______________________________________
- [ ] Recorded BIOS/UEFI vendor, version/date: __________________________________
- [ ] Identified boot mode: [ ] UEFI  [ ] Legacy  [ ] Not exposed
- [ ] External visual check (physical PC, if safe): cables/vents/status LEDs; notes: __________

## 2. Operating-system inventory

- [ ] Confirmed OS name/version and architecture (`msinfo32` / `hostnamectl`).
- [ ] Recorded CPU model and cores/threads (`Get-CimInstance` / `lscpu`).
- [ ] Recorded RAM total and/or modules (`Get-CimInstance` / `free -h`).
- [ ] Recorded disk model/capacity (`Get-CimInstance` / `lsblk`).
- [ ] Recorded firmware version from OS (`Get-CimInstance Win32_BIOS` / `dmidecode`).
- [ ] Checked OS boot mode and Secure Boot if available (`msinfo32` / Linux EFI check).
- [ ] Checked Windows Device Manager warning icons, or noted equivalent Linux issues.

## 3. Compare, document, publish

- [ ] Compared firmware or VM allocations against OS-detected CPU, RAM, and disks.
- [ ] Explained discrepancies (e.g. memory reservation, decimal/binary units, virtual devices).
- [ ] Added redacted screenshot(s) or written observation(s); no personal identifiers.
- [ ] Completed `reports/my-inspection.md` with actual evidence and findings.
- [ ] Checked GitHub files for serial numbers, names, hostnames, IPs, MACs, keys.

**Summary / findings:** _________________________________________________________  
**Action / follow-up:** _________________________________________________________  
**Result:** [ ] Completed  [ ] In progress  [ ] Blocked (explain in report)
