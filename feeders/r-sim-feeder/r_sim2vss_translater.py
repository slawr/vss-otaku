#!/usr/bin/env python3

# Translation between the Renesas Connected Car Simulator and VSS data models
#
# Copyright (C) 2021 Renesas Electronics Corporation
#
# Status: In development. Model may not match all possible simulator output.
# VSS data model version: FIXME v2.2+ (commit 14e59425c12d)
# Simulator data model version: Connected SDK v1.6

def translate_geometry(arg):
    result = {}

    # arg.geometry.coordinates.Latitude
    result['Vehicle.CurrentLocation.Latitude'] = float(arg['coordinates']['Latitude'])

    # arg.geometry.coordinates.Longitude
    result['Vehicle.CurrentLocation.Longitude'] = float(arg['coordinates']['Longitude'])

    return result

# Return python dictionary of key/value pairs in the VSS data model
def translate(arg):
    return translate_geometry(arg['geometry'])