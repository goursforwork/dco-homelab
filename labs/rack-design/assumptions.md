# Rack Design Assumptions

## Purpose

This file documents the assumptions used in the simulated rack design so that the design can be reviewed consistently.

## Physical Rack

- Standard 19-inch rack
- 42U total rack height
- Three 2U rack servers
- Two 1U network switches
- Two 1U patch panels
- Additional rack space reserved for future expansion and cable management
- Rails and server depth are assumed to be compatible with the rack

## Server Assumptions

Each server is assumed to have:

- Two network interfaces used for redundant network paths
- Two hot-swappable power supplies
- 1+1 PSU redundancy
- One PSU capable of supporting the server's required operating load
- Front-to-rear airflow
- Standard out-of-band management capability such as iDRAC, iLO, or equivalent, although management cabling is not shown in the base diagram

## Network Assumptions

- Switch A and Switch B are separate physical switches
- Each server has one network path to each switch
- Patch Panel A is associated with the Switch A path
- Patch Panel B is associated with the Switch B path
- The two switch paths are intended to reduce single-switch dependency
- Seamless failover is not assumed solely from cabling
- Host bonding/teaming, switch configuration, VLANs, routing, LACP, or application redundancy would be configured as required in a real environment

## Power Assumptions

- PDU A and PDU B are separate rack PDUs
- PDU A is supplied by Power Feed A
- PDU B is supplied by Power Feed B
- Power Feed A and Power Feed B are treated as separate failure domains
- UPS A supports Feed A
- UPS B supports Feed B
- Server PSU 1 connects to PDU A
- Server PSU 2 connects to PDU B
- A single PSU or single PDU failure should not power off a server, provided remaining capacity is sufficient

## Airflow Assumptions

- Servers use front-to-rear airflow
- Cold air enters from the rack front
- Hot exhaust leaves from the rack rear
- Switch airflow is assumed to be aligned with the rack airflow
- In a real rack, blanking panels would be used where appropriate to reduce hot-air recirculation

## Scope Limitations

This lab does not model:

- Real production data-center architecture
- Production workloads
- Actual electrical load calculations
- Breaker sizing
- UPS runtime calculations
- Generator systems
- Real switch configuration
- STP/MLAG/vPC design
- VLAN/IP addressing
- Storage networking
- Out-of-band management network
- Fire suppression
- Environmental monitoring
- Physical security controls

## Portfolio Disclaimer

This is a self-directed simulated infrastructure project created for hands-on learning and portfolio demonstration.
