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
    s_by_distance = []
    for station in stations:
        # Calculates distances of station locations from p and arranges them in a list
        distance = haversine(station.coord, p, unit=Unit.KILOMETERS)
        s_by_distance.append((station, distance))

        # Sorts stations by distance from p
        sorted_stations = sorted_by_key(s_by_distance, 1)
    return sorted_stations

def stations_within_radius(stations, centre, r):
    """Returns a list of all stations within radius r of a geographic coordinate centre"""
    s_within_radius = []
    for station in stations:
        # Calculates distances of station locations from centre
        distance = haversine(station.coord, centre, unit=Unit.KILOMETERS)

        # Discards stations not within the given radius
        if distance < r:
            s_within_radius.append(station)

    return s_within_radius

def rivers_with_station(stations):
    """Returns a set with the names of rivers with a monitoring station"""
    rivers = {}
    for station in stations:
        rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    pass

def rivers_by_station_number(stations, N):
    pass
