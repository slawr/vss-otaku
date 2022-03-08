#!/usr/bin/env python3

# VSS Data Store functions for Apache IoTDB timeseries DB
#
# Copyright (C) 2022 Renesas Electronics Corporation
#
# Status: In development.

from iotdb.Session import Session
from iotdb.utils.IoTDBConstants import TSDataType, TSEncoding, Compressor
from iotdb.utils.Tablet import Tablet

def vss_insert_aligned(data):
    # Insert (write) VSS formatted aligned TS payload using Python client session API
    for i in data:
        print(f'INSERT {i}')
