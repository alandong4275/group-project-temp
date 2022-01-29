# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine, Unit
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    """Calculates distance of stations in km from a coordinate p"""
    distances = []
    for station in stations: 
        distance = haversine(station.coord, p, unit=Unit.KILOMETERS)
        distances.append((station, distance))
        sorted_by_key(distances, 1)
    return distances
