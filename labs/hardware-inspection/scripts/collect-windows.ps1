# Read-only hardware inventory for Windows PowerShell.
# Intentionally does not request serial numbers, hostnames, MAC/IP addresses, or usernames.
# Inspect the displayed output before copying any of it into public documentation.

function Show-Section([string]$Title) {
    Write-Output ""
    Write-Output "=== $Title ==="
}

Show-Section 'SYSTEM / RAM TOTAL'
Get-CimInstance -ClassName Win32_ComputerSystem |
    Select-Object Manufacturer, Model, @{Name='InstalledRAM_GiB';Expression={[math]::Round($_.TotalPhysicalMemory / 1GB, 2)}} |
    Format-List | Out-String | Write-Output

Show-Section 'CPU'
Get-CimInstance -ClassName Win32_Processor |
    Select-Object Name, NumberOfCores, NumberOfLogicalProcessors |
    Format-List | Out-String | Write-Output

Show-Section 'MEMORY MODULES'
Get-CimInstance -ClassName Win32_PhysicalMemory |
    Select-Object @{Name='Capacity_GiB';Expression={[math]::Round($_.Capacity / 1GB, 2)}}, Speed, Manufacturer |
    Format-Table -AutoSize | Out-String | Write-Output

Show-Section 'DISKS'
Get-CimInstance -ClassName Win32_DiskDrive |
    Select-Object Model, MediaType, @{Name='Capacity_GiB';Expression={[math]::Round($_.Size / 1GB, 2)}} |
    Format-Table -AutoSize | Out-String | Write-Output

Show-Section 'BIOS / UEFI METADATA (NOT BOOT MODE)'
Get-CimInstance -ClassName Win32_BIOS |
    Select-Object Manufacturer, SMBIOSBIOSVersion, ReleaseDate |
    Format-List | Out-String | Write-Output

Show-Section 'OPERATING SYSTEM'
Get-CimInstance -ClassName Win32_OperatingSystem |
    Select-Object Caption, Version, OSArchitecture |
    Format-List | Out-String | Write-Output

Write-Output 'Manual follow-up: run msinfo32 and record BIOS Mode, Secure Boot State, and physical/VM firmware observations.'
Write-Output 'Review all fields before sharing publicly; data can still identify hardware models.'
