from floodsystem.stationdata import build_station_list
from floodsystem import station

def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    # Creates list of stations with inconsistent typical ranges
    inconsistent_stations = list()
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent_stations.append(station.name)
        else:
            pass

    # Sorts list alphabetically
    inconsistent_stations.sort()

    # Displays list
    print("Monitoring stations with inconsistent typical ranges:")
    print(inconsistent_stations)


if __name__ == "__main__":
    print("\n" + "*** Task 1F: CUED Part IA Flood Warning System ***" + "\n")
    run()

