# VSS Otaku

vss-otaku is a hacking playground to prototype various tools related to the [Covesa](https://www.covesa.global/)/W3C [Vehicle Signal Specification (VSS)](https://github.com/COVESA/vehicle_signal_specification). Using patterns and tooling from the [vss-tools](https://github.com/COVESA/vss-tools) eco-system and the [Common Vehicle Interface Initiative (CVII) Tech Stack](
https://at.projects.genivi.org/wiki/display/MIG/CVII+Tech+Stack).

The intention would be to migrate productive/mature work upstream into vss-tools, or as a separate component if vss-tools is not a good fit.

For both of those reasons this is unlikely to be a place for stable releases. Code may change often, possibly breaking backwards compatibility. Commits may be force pushed as terraforming of ideas takes shape.

## Current areas of interest
Closing the gap between data sources and in-vehicle Data Servers. As a starting point Southbound VSS-feeders from the Renesas Simulator and CAN towards/into VSS data are being investigated.

In-vehicle storage of VSS data using a time series database such as [Apache IoTDB](https://iotdb.apache.org/). Then the use of such a database as a backend into data servers such as [VISS](https://www.w3.org/TR/vehicle-information-service/) or [GraphQL](https://github.com/COVESA/graphql-vss-data-server).

This is likely to break down into two main technical areas:
1. Format Converters and Code Generators to automate conversion of formats such as data models into forms to be consumed by other processes. For example, generation of C++ code to convert input data into VSS.
2. Data Feeders that connect in-vehicle data sources to VSS Data Servers and Storage using the automation from the first area. A goal is pluggable components that can be reusable in different configurations.

For details see the documentation in the sub-directories.

## Contributions
If you have issues or fixes, then please raise them in Github as Issues or Pull Requests.

If you have something major in mind then perhaps we should discuss it first, possibly upstream in the Covesa CVII project. Others may have good input or be willing to help.

## Why the name VSS Otaku?
[Otaku](https://en.wikipedia.org/wiki/Otaku) is a Japanese word describing someone with a consuming interest in a particular subject. Although commonly attached to Anime and Manga, Otaku can be interested in a wide range of subjects. Having a passion for the beauty and artistry that goes into the creation of a [Maki-e fountain pen](https://www.pilot-namiki.com/en/) could mean you are a Maki-e Otaku.

In popular slang it is often translated to Geek or Nerd in English and as with those words can have both negative and positive interpretations. At the same time we see people reclaiming positive interpretations to counter the alternative use as a pejorative. In that spirit I use Otaku as a positive description of a consuming focus on VSS for the people involved in this project.