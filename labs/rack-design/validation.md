# Rack Design Validation Plan

## Purpose

Validate that the simulated rack design meets its intended redundancy and documentation goals.

> These tests describe expected behavior. In a physical lab, each result should be recorded with date, outcome, evidence, and notes.

---

## Test 1 — Rack Layout Review

### Procedure

1. Confirm the diagram contains three servers.
2. Confirm it contains two switches.
3. Confirm it contains two patch panels.
4. Confirm equipment is assigned to rack units.
5. Confirm future expansion space exists.

### Expected Result

All required rack components are present and rack-unit assignments do not overlap.

### Status

- [ ] Pass
- [ ] Fail

---

## Test 2 — Server Dual-Network Path Review

### Procedure

For each server:

1. Verify NIC 1 connects to Switch A.
2. Verify NIC 2 connects to Switch B.
3. Verify cable labels are unique.

### Expected Result

Every server has two separate physical network paths.

### Status

- [ ] Pass
- [ ] Fail

---

## Test 3 — Switch A Failure Scenario

### Simulated Failure

Switch A becomes unavailable.

### Expected Result

The physical path through NIC 2 and Switch B remains available for all three servers.

### Important Note

Actual application or IP connectivity depends on logical configuration such as NIC teaming/bonding, routing, VLANs, and switch design.

### Status

- [ ] Pass
- [ ] Fail

---

## Test 4 — Switch B Failure Scenario

### Simulated Failure

Switch B becomes unavailable.

### Expected Result

The physical path through NIC 1 and Switch A remains available for all three servers.

### Status

- [ ] Pass
- [ ] Fail

---

## Test 5 — PSU Failure Scenario

### Simulated Failure

Server 2 PSU 1 fails.

### Expected Result

Server 2 remains powered through PSU 2, assuming PSU 2 is healthy and sized to carry the required load.

### Status

- [ ] Pass
- [ ] Fail

---

## Test 6 — PDU A Failure Scenario

### Simulated Failure

PDU A loses power.

### Expected Result

All three servers remain powered through their PSU 2 connections to PDU B.

### Status

- [ ] Pass
- [ ] Fail

---

## Test 7 — PDU B Failure Scenario

### Simulated Failure

PDU B loses power.

### Expected Result

All three servers remain powered through their PSU 1 connections to PDU A.

### Status

- [ ] Pass
- [ ] Fail

---

## Test 8 — Power-Path Diversity Review

### Procedure

For each server:

1. Confirm PSU 1 connects to PDU A.
2. Confirm PSU 2 connects to PDU B.
3. Confirm both PSUs are not connected to the same PDU.

### Expected Result

No server depends on a single rack PDU for both redundant PSUs.

### Status

- [ ] Pass
- [ ] Fail

---

## Test 9 — Airflow Review

### Procedure

1. Confirm server intake faces the cold aisle/front.
2. Confirm exhaust faces the hot aisle/rear.
3. Confirm switches follow compatible airflow direction.
4. Confirm cables do not obstruct intake or exhaust areas.

### Expected Result

The design supports consistent front-to-rear airflow.

### Status

- [ ] Pass
- [ ] Fail

---

## Test 10 — Documentation Review

### Procedure

Confirm the repository includes:

- README.md
- rack-diagram.png
- assumptions.md
- cabling-map.md
- validation.md

### Expected Result

All project documentation is present and internally consistent.

### Status

- [ ] Pass
- [ ] Fail

---

## Validation Record

| Test | Result | Evidence / Notes |
|---|---|---|
| Rack layout | Not tested | |
| Dual network paths | Not tested | |
| Switch A failure | Not tested | |
| Switch B failure | Not tested | |
| PSU failure | Not tested | |
| PDU A failure | Not tested | |
| PDU B failure | Not tested | |
| Power-path diversity | Not tested | |
| Airflow | Not tested | |
| Documentation | Not tested | |

---

## Lessons Learned

Record findings after completing the exercise:

- What single points of failure were identified?
- Did the physical and logical redundancy assumptions match?
- Were any cable labels ambiguous?
- Was rack space used efficiently?
- Were power A/B paths clearly separated?
- What would be added in a production-grade design?
