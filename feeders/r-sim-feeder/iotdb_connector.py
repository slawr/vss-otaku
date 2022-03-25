#!/usr/bin/env python3

# VSS Data Store functions for Apache IoTDB timeseries DB
#
# Copyright (C) 2022 Renesas Electronics Corporation
#
# Status: In development.

from ctypes.wintypes import BOOLEAN
from iotdb.Session import Session
from iotdb.utils.IoTDBConstants import TSDataType, TSEncoding, Compressor
from iotdb.utils.Tablet import Tablet

# Simple iotdb session configuration
ip = "127.0.0.1"
port_ = "6667"
username_ = "root"
password_ = "root"
session = Session(ip, port_, username_, password_, fetch_size=1024, zone_id="GMT+00:00")
device_id_ = "root.sg_test_01.d_01"

# Simple schema
iotdb_vss_leaf_keys = [
    '"Vehicle.CurrentLocation.Latitude"',
    '"Vehicle.CurrentLocation.Longitude"',
]

iotdb_vss_value_types = [
    TSDataType.FLOAT,
    TSDataType.FLOAT,
]

encoding_lst_ = [TSEncoding.PLAIN for _ in range(len(iotdb_vss_value_types))]
compressor_lst_ = [Compressor.SNAPPY for _ in range(len(iotdb_vss_value_types))]

# Public Methods
def create_time_series():

    # create_time_series() requires a list of full TS paths. Create one from
    # concatenation of device_id + vss leaf node keys
    ts_path_lst_ = []
    for i in iotdb_vss_leaf_keys:
        ts_path = '{}."{}"'.format(device_id_, i)
        ts_path_lst_ += {ts_path}

    session.create_multi_time_series(ts_path_lst_, iotdb_vss_value_types, encoding_lst_, compressor_lst_)

def create_aligned_time_series():
    # FIXME: The multiple readings per timesclice delivered by the sim input
    # makes more sense for this feeder, but the API does not appear until
    # iotdb v0.13. Update to it when v0.13 released
    session.create_aligned_time_series(
        device_id_, iotdb_vss_leaf_keys, iotdb_vss_value_types, encoding_lst_, compressor_lst_
)

# Input: TS, dictionary of key/value pairs
def insert_vss_ts(timestamp_, data):
    # Build array of VSS leaf node values
    values_ = []
    values_ = list(data.values())

    session.insert_record(device_id_, timestamp_, iotdb_vss_leaf_keys, iotdb_vss_value_types, values_)

def open_session():
    session.open(False)

def close_session():
    session.close()

def insert_vss_aligned(data):
    # Insert (write) VSS formatted aligned TS payload using Python client session API
    for i in data:
        session.insert_aligned_record

def vss_print_aligned(data):
    # Print out VSS formatted aligned data
    for i in data:
        print(f'INSERT {i}')

# Private Methods
#def generate_schema():
