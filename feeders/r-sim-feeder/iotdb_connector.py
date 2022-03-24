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
vss_node_lst = [
    '"Vehicle.CurrentLocation.Latitude"',
    '"Vehicle.CurrentLocation.Longitude"',
]

vss_node_type_lst = [
    TSDataType.FLOAT,
    TSDataType.FLOAT,
]

encoding_lst_ = [TSEncoding.PLAIN for _ in range(len(vss_node_type_lst))]
compressor_lst_ = [Compressor.SNAPPY for _ in range(len(vss_node_type_lst))]

# Public Methods
def create_time_series():

    # create_time_series() requires a list of full TS paths. Create one from
    # concatenation of device_id + vss leaf node keys
    ts_path_lst_ = []
    for i in vss_node_lst:
#        ts_path = ".".join([device_id_, i])
        ts_path = '{}."{}"'.format(device_id_, i)
        ts_path_lst_ += {ts_path}

    session.create_multi_time_series(ts_path_lst_, vss_node_type_lst, encoding_lst_, compressor_lst_)

def create_aligned_time_series():
    # FIXME: The multiple readings per timesclice delivered by the sim input
    # makes more sense for this feeder, but the API does not appear until
    # iotdb v0.13. Update to it when v0.13 released
    session.create_aligned_time_series(
        device_id_, vss_node_lst, vss_node_type_lst, encoding_lst_, compressor_lst_
)

# FIXME: Little hack to get values from the data array. It works for this now but needs
# replacing later with proper value lookup, i.e. replace this completly.
def get_value(data, path):
    for i in data:
        if i['path'] == path:
            return i['value']

def insert_vss_ts(timestamp_, data):
    # Build array of VSS leaf node values
    values_ = []
    for x in vss_node_lst:
        # Strip double quotes used in IoTDB sensor name as it is not present in the data
        x = x.strip('\"')
        values_ += {get_value(data, x)}

    session.insert_record(device_id_, timestamp_, vss_node_lst, vss_node_type_lst, values_)

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
#def generate_type_mapping():
