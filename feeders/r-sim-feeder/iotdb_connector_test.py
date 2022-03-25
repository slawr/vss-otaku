#!/usr/bin/env python3

# Test module for iotdb_connector.py (Apache IoTDB connector)
#
# Copyright (C) 2022 Renesas Electronics Corporation

import iotdb_connector

timestamp = 1637868968335
data = {
    # arg.geometry.coordinates.Latitude
    'Vehicle.CurrentLocation.Latitude' : 40.76579,
    # arg.geometry.coordinates.Longitude
    'Vehicle.CurrentLocation.Longitude' : -73.9873
    }

if __name__ == "__main__":
    # Connect to the IoTDB Server
    iotdb_connector.open_session()

    # Create TS schema
#    iotdb_connector.create_time_series()

    # Insert TS data
    iotdb_connector.insert_vss_ts(timestamp, data)

    # Close connection
    iotdb_connector.close_session()