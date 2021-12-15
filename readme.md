# VSS Otaku

vss-otaku is a hacking playground to prototype various tools related to the Covesa/W3C Vehicle Signal Specification (VSS). Using patterns and tooling from the vss-tools eco-system.

The intention would be to migrate productive/mature work upstream into vss-tools

## Current areas of interest

Southbound feeders from the Renesas Simulator and CAN towards/into VSS data.

In-vehicle storage of VSS data using a time series database such as Apache iotdb. Then the use of such a DB as a backend into data servers such as VISS or GraphQL.