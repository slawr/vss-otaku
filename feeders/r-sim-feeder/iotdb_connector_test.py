#!/usr/bin/env python3

# Test module for iotdb_connector.py (Apache IoTDB connector)
#
# Copyright (C) 2022 Renesas Electronics Corporation

import iotdb_connector

timestamp = 1637868968335
data = [
        # arg.geometry.coordinates.Latitude
        {
            'path': 'Vehicle.CurrentLocation.Latitude',
            'value': -73.9873
        },
        # arg.geometry.coordinates.Longitude
        {
            'path': 'Vehicle.CurrentLocation.Longitude',
            'value': 40.76579
        }
    ]

if __name__ == "__main__":
    # Connect to the IoTDB Server
    iotdb_connector.open_session()

    # Create TS schema
#    iotdb_connector.create_time_series()

    # Insert TS data
    iotdb_connector.insert_vss_ts(timestamp, data)

    # Close connection
    iotdb_connector.close_session()