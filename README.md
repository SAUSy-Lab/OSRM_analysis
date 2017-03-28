## OSRM_analysis
Scripts for batch routing analysis using OSRM (Open Source Routing Machine)

The following provides quick instructions to get OSRM up and running, and then some description of a few scripts used for batch routing computations. Most of these are written in Python.

#### OSRM Installation

Quickly ..

```
git clone https://github.com/Project-OSRM/osrm-backend.git
cd osrm-backend
```

```
mkdir -p build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build .
sudo cmake --build . --target install
```

For more info:
https://github.com/Project-OSRM/osrm-backend/wiki/Building-OSRM

Ubuntu will need the following dependencies:
https://github.com/Project-OSRM/osrm-backend/wiki/Building-on-Ubuntu

#### Getting Data and Starting the Machine:

OSRM takes OpenStreetMap (OSM) data as the input to build the network graph.

The script, osm_from_extents.py, contains a function to download OSM data via bounding box extents with wget. It has an extension of grab the extents of list of coordinates in a .csv table.

```
osrm-extract osrm/map.osm.xml -p osrm/profiles/bicycle.lua
osrm-contract osrm/map.osrm
osrm-routed osrm/map.osrm
```

These are included in a few shell scripts, separated by walk, bike, and drive.

#### Simple Requests:

Official documentation:
http://project-osrm.org/docs/v5.5.2/api/#general-options

#### Batch Scripts:

And without further Apu, here are some python

trip_geom.py = batch outputs trip geometries and travel attributes for one-to-many analysis




--
