from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.utils import sorted_by_key


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Creates list of stations sorted by distance from Cambridge city centre
    station_names_within_radius = sorted_by_key([station.name for station in stations_within_radius(stations,  (52.2053, 0.1218), 10)], 0)

    # Displays list
    print("Stations within radius:")
    print(station_names_within_radius)


if __name__ == "__main__":
    print("\n" + "*** Task 1C: CUED Part IA Flood Warning System ***" + "\n")
    run()

