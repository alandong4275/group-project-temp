from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Returns list of stations sorted by distance from Cambridge city centre
    sorted_stations = stations_by_distance(stations,  (52.2053, 0.1218))

    # Creates two lists of the 10 closest stations and 10 furthest stations, their closest towns, 
    # and their distance from Cambridge city centre
    closest_stations = [(station.name, station.town, distance) for (station, distance) in sorted_stations[:10]]
    furthest_stations = [(station.name, station.town, distance) for (station, distance) in sorted_stations[-10:]]

    # Displays two lists
    print(closest_stations)
    print(furthest_stations)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

