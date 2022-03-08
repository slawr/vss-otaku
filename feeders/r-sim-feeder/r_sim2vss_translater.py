#!/usr/bin/env python3

# Translation between the Renesas Connected Car Simulator and VSS data models
#
# Copyright (C) 2021 Renesas Electronics Corporation
#
# Status: In development. Model may not match all possible simulator output.
# VSS data model version: FIXME v2.2+ (commit 14e59425c12d)
# Simulator data model version: Connected SDK v1.6

def translate_geometry(arg):
    result = []

    return result + [
        # arg.geometry.coordinates.Latitude
        {
            'path': 'Vehicle.CurrentLocation.Latitude',
            'value': float(arg['coordinates']['Latitude'])
        },
        # arg.geometry.coordinates.Longitude
        {
            'path': 'Vehicle.CurrentLocation.Longitude',
            'value': float(arg['coordinates']['Longitude'])
        }
    ]


def translate(arg):
    result = []
    result += translate_geometry(arg['geometry'])

    return result