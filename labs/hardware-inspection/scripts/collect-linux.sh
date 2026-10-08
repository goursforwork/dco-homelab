#!/usr/bin/env bash
# Read-only Linux inventory. Intentionally omits commands that print serials, hostnames, or network IDs.
# Review output before sharing publicly.
set -u
section() { printf '\n=== %s ===\n' "$1"; }

section 'OS'
if command -v lsb_release >/dev/null 2>&1; then lsb_release -d; elif [ -r /etc/os-release ]; then grep '^PRETTY_NAME=' /etc/os-release; else uname -s; fi
uname -m

section 'CPU'
if command -v lscpu >/dev/null 2>&1; then
  lscpu | grep -E '^(Architecture|CPU\(s\)|Model name|Thread\(s\) per core|Core\(s\) per socket|Socket\(s\)):' || true
else
  echo 'lscpu unavailable'
fi

section 'MEMORY'
if command -v free >/dev/null 2>&1; then free -h; else echo 'free unavailable'; fi

section 'DISKS'
if command -v lsblk >/dev/null 2>&1; then lsblk -o NAME,SIZE,TYPE,MODEL; else echo 'lsblk unavailable'; fi

section 'BOOT MODE'
if [ -d /sys/firmware/efi ]; then
  echo 'UEFI environment detected by running OS'
else
  echo 'UEFI directory absent (legacy boot, unsupported guest, or unavailable)'
fi

section 'FIRMWARE (OPTIONAL; REQUIRES ROOT FOR DMI)'
if command -v dmidecode >/dev/null 2>&1; then
  echo 'When authorized, run: sudo dmidecode -s bios-vendor'
  echo 'When authorized, run: sudo dmidecode -s bios-version'
  echo 'When authorized, run: sudo dmidecode -s bios-release-date'
else
  echo 'dmidecode is not installed; record not available'
fi

echo 'Review output and remove identifiers before publication.'
