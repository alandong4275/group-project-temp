from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Creates list of rivers with stations
    rivers = rivers_with_station(stations)

    # Creates list of stations by rivers
    s_by_rivers = stations_by_river(stations)

    # Displays lists
    print(rivers)
    print(s_by_rivers)


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

