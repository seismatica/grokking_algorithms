from pprint import pprint

states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
stations = {
    'kfour': {'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kone': {'id', 'nv', 'ut'},
    'kthree': {'or', 'nv', 'ca'},
    'kfive': {'ca', 'az'}
}
final_stations = set()


def find_best_stations(states, stations):
    """
    Find list of stations that will cover all specified states
    :param states: list of states that need to be covered
    :param stations: dict of station:states covered by station
    :return: list of stations that will cover all specified states
    """
    # Create mutable copies of states and stations to be modified when loop is run, and keep the original copies intact
    states_needed = states.copy()
    available_stations = stations.copy()

    while states_needed:
        print(states_needed)
        best_station = None
        best_covered = set()

        # If number of needed states covered by any station is higher than current number of covered states,
        # set that station as current best station and states covered by that station as best covered
        for station, states_per_station in available_stations.items():
            covered = states_needed & states_per_station
            if len(covered) > len(best_covered):
                best_station = station
                best_covered = covered

        # Add best station to final station list, and remove states covered by best station from list of states needed
        final_stations.add(best_station)
        print(best_station, best_covered)
        states_needed -= best_covered

        # Technically this is not needed as stations from best station has been excluded from list of states needed
        # Therefore, there will be zero intersection ({}) between states_needed states_per_station for that station
        del available_stations[best_station]

    return final_stations


print(find_best_stations(states_needed, stations))


