from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""
    stations = build_station_list()
    sorted_stations = stations_by_distance(stations,  (52.2053, 0.1218))
    closest_stations = [(station.name, station.town, distance) for (station, distance) in sorted_stations[:10]]
    furthest_stations = [(station.name, station.town, distance) for (station, distance) in sorted_stations[-10:]]
    print(closest_stations)
    print(furthest_stations)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()