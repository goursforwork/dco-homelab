# Hardware Inspection & System Inventory

**Lab type:** Read-only inventory and validation | **Platform:** Windows PC, Linux host, or VM guest  

## Objective

Inspect a physical PC or VM using BIOS/UEFI (or virtual firmware configuration) and OS-level tools. Identify the CPU, memory, storage, manufacturer/model, BIOS version, boot mode, and any discrepancies, then produce a concise one-page inspection checklist and a findings report. This reflects common server-asset documentation and first-line troubleshooting tasks.

## Deliverables

1. [Printable one-page inspection checklist](checklists/hardware-inspection-checklist.pdf)
2. [Editable checklist](checklists/hardware-inspection-checklist.md), 
3. [Inspection report](reports/inspection-report-template.md), copied to `reports/my-inspection.md`
4. Optional redacted screenshots under `evidence/` with a short explanation of each

> **Privacy:** Never publish BIOS/system serial numbers, asset tags, hostnames, user names, network addresses, MAC addresses, BitLocker recovery keys, passwords, or unredacted desktop screenshots. Inventory commands here intentionally avoid requesting serial numbers. Review even sanitized output before sharing.

## Prerequisites

- A PC or VM you are authorized to inspect; ordinary user access is sufficient for most Windows commands
- PowerShell on Windows; basic terminal on Linux
- Optional: `dmidecode` on Linux, which generally requires root privileges
- GitHub account if you want a public portfolio repository

## Procedure

### 1. Identify the lab environment

Record the inspection date, `physical PC` vs `VM guest`, the operating system, and the hypervisor if applicable. **In a VM, the guest may expose virtual CPU, RAM, disks, and BIOS/UEFI — these are not necessarily the physical host's specifications.** Do not describe VM guest output as a physical-host audit.

### 2. Inspect BIOS/UEFI or virtual firmware

**Physical PC:** Reboot and use your vendor's firmware key (often F2, Del, or Esc), or in Windows use **Settings > System > Recovery > Advanced startup > Restart now > Troubleshoot > Advanced options > UEFI Firmware Settings**, if available. Find firmware/System Information pages and record: CPU model, RAM capacity, detected storage, BIOS version/date, and boot/UEFI status when displayed. Take a photograph if permitted. **Do not change firmware settings.**

**VM:** Check the hypervisor's VM settings and note allocated vCPU, memory, virtual disk size and guest firmware mode (UEFI/legacy). Some VMs will not offer a traditional firmware UI or may show minimal details. Record `not exposed` rather than guessing.

### 3. Windows OS inventory

Launch `msinfo32` (`Win + R` > `msinfo32`) and capture **System Manufacturer, System Model, BIOS Version/Date, BIOS Mode, Installed Physical Memory, Secure Boot State**, where exposed. In PowerShell, execute each of the following:

```powershell
Get-CimInstance Win32_ComputerSystem | Select-Object Manufacturer,Model,TotalPhysicalMemory
Get-CimInstance Win32_Processor | Select-Object Name,NumberOfCores,NumberOfLogicalProcessors
Get-CimInstance Win32_PhysicalMemory | Select-Object Manufacturer,Capacity,Speed
Get-CimInstance Win32_DiskDrive | Select-Object Model,MediaType,Size
Get-CimInstance Win32_BIOS | Select-Object Manufacturer,SMBIOSBIOSVersion,ReleaseDate
Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,OSArchitecture
```

For optional convenience, run `scripts/collect-windows.ps1` in PowerShell (review the script before executing). `devmgmt.msc` opens Device Manager so you can visually check for warning icons. If script execution is restricted, use the individual commands above rather than weakening security policies.

**Unit check:** `Capacity` and `Size` are normally reported in **bytes**, not GB. Divide by `1GB` in PowerShell to display GiB, or document the units explicitly. Storage vendors commonly advertise decimal GB; Windows commonly shows GiB.

### 4. Linux OS inventory

```bash
hostnamectl
lscpu
free -h
lsblk -o NAME,SIZE,TYPE,MODEL
[ -d /sys/firmware/efi ] && echo 'UEFI booted' || echo 'Legacy / UEFI not detected'
sudo dmidecode -t bios         # Optional; requires package and permission
```

You can also run `bash scripts/collect-linux.sh`, which avoids serial-number fields. If the guest cannot expose a firmware field, record `not available`.

### 5. Validate and troubleshoot

Compare the firmware/hypervisor values to the OS values: CPU, installed RAM, boot mode, and detected storage. If they differ, document a *plausible explanation* such as allocated vs host capacity, reserved memory, decimal vs binary capacity, or the guest only seeing assigned virtual hardware. Do not declare a hardware defect without diagnostic evidence. Record Device Manager warnings or inaccessible devices separately.

### 6. Produce evidence and a finished report

- Fill out `checklists/hardware-inspection-checklist.md` and/or print its PDF version.
- Copy `reports/inspection-report-template.md` to `reports/my-inspection.md` and enter actual results. Replace uncompleted `TBD` values; label `not available` clearly.
- If you share screenshots, redact private details and place files under `evidence/`. Add references to them in your report.
- Write at least one finding or record `No discrepancies observed in the items checked` if that is supported by your observations.

## Definition of done

- [ ] At least one BIOS/UEFI or virtual firmware observation documented
- [ ] CPU, RAM, storage, OS, and BIOS version captured using OS tools
- [ ] Firmware vs OS comparison completed or unavailable fields explicitly noted
- [ ] One-page checklist dated and marked
- [ ] Report includes evidence references, findings, and next action
- [ ] Public repository reviewed for personal, system, or network identifiers

