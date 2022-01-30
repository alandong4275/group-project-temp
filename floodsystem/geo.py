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

    s_by_distance = list()
    for station in stations:
        # Calculates distances of station locations from p and arranges them in a list
        distance = haversine(station.coord, p, unit=Unit.KILOMETERS)
        s_by_distance.append((station, distance))

        # Sorts stations by ascending distance from p
        sorted_stations = sorted_by_key(s_by_distance, 1)

    return sorted_stations

def stations_within_radius(stations, centre, r):
    """Returns a list of all stations within radius r of a geographic coordinate centre"""

    s_within_radius = list()
    for station in stations:
        # Calculates distances of station locations from centre
        distance = haversine(station.coord, centre, unit=Unit.KILOMETERS)

        # Discards stations not within the given radius
        if distance < r:
            s_within_radius.append(station)

    return s_within_radius

def rivers_with_station(stations):
    """Returns a list of the names of rivers with a monitoring station"""

    # Creates a set of rivers with monitoring stations
    rivers = set()
    for station in stations:
        if station.river != None:
            rivers.add(station.river)
    
    # Converts set into alphabetically ordered list
    sorted_rivers = sorted(rivers)

    return sorted_rivers

def stations_by_river(stations):
    """Returns a dictionary mapping the names of rivers with a list of their monitoring station"""

    # Creates a dictionary of rivers that map to a list of their monitoring stations
    rivers = dict()
    for station in stations:
        # Adds names of monitoring stations into the list under each river
        if station.river != None:
            if station.river in rivers.keys():
                rivers[station.river].append(station.name)
            else:
                rivers[station.river] = [station.name]
        else:
            pass

    # Sorts the lists of monitoring stations alphabetically
    for river in rivers.keys():
        rivers[river].sort()

    return rivers


def rivers_by_station_number(stations, N):
    """Returns a list of the N rivers with the greatest number of monitoring stations 
    and their number of monitoring stations"""

    # Creates a dictionary of rivers that map to their number of monitoring stations
    rivers = dict()
    for station in stations:
        # Increments number of monitoring stations by 1 for each new monitoring station by a given river
        if station.river != None:
            if station.river in rivers.keys():
                rivers[station.river] += 1
            else:
                rivers[station.river] = 1
        else:
            pass
    
    # Converts dictionary into list of tuples
    river_list  = [(key, value) for key, value in rivers.items()]

    # Sorts list by descending number of monitoring stations
    sorted_rivers = sorted_by_key(river_list, 1, reverse=True)

    # Truncates list to initial N items
    greatest_rivers = sorted_rivers[:N]

    return greatest_rivers

