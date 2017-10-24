from pprint import pprint
from operator import itemgetter


def djikstra(graph, start, end):
    nodes = list(graph.keys())
    nodes.remove(start)
    start_neighbors = graph[start]

    def build_parents_dict():
        """
        Build dict of parents from a dict of graph
        :return: dict containing nodes (except for starting node) as keys and their parent as value
        """
        parents = {}

        for node in nodes:
            if node in start_neighbors.keys():
                parents[node] = start
            else:
                parents[node] = None

        return parents

    def build_costs_dict():
        """
        Build dict of costs from a dict of graph
        :return: dict containing nodes (except for starting node) as keys and their cost (from start node) as value
        """
        infinity = float('inf')
        costs = {}

        for node in nodes:
            if node in start_neighbors.keys():
                costs[node] = start_neighbors[node]
            else:
                costs[node] = infinity

        return costs

    def display_shortest_path(start, end):
        """
        Display path from start to end and length of total path
        :return: print path from start to end and length of total path
        """
        # print(end, start)
        if parents[end] == start:
            return start + ' -> ' + end
        else:
            parent = parents[end]
            str = display_shortest_path(start, parent) + ' -> ' + end
            return str


    parents = build_parents_dict()
    costs = build_costs_dict()
    costs_copy = costs.copy()
    processed = []

    while nodes:
        # Find node with lowest cost from start
        cheapest_node, cheapest_cost = min(costs_copy.items(), key=itemgetter(1))

        # Find neighbors:distance of cheapest node from graph
        neighbors = graph[cheapest_node]

        # Add distance to neighbor and node cost, and compare it with current cost of neighbor
        # If the added cost is lower, replace current cost of neighbor with it
        for neighbor in neighbors.keys():
            cheapest_to_neighbor = neighbors[neighbor]
            new_cost = cheapest_cost + cheapest_to_neighbor
            current_cost = costs[neighbor]

            if new_cost < current_cost:
                costs[neighbor] = new_cost
                costs_copy[neighbor] = new_cost
                parents[neighbor] = cheapest_node

        # Delete processed note from node list and cost copy (so cheapest node will only be looked up among
        # unprocessed nodes). Update list of processed nodes.
        nodes.remove(cheapest_node)
        del costs_copy[cheapest_node]
        processed.append(cheapest_node)


    shortest_path = display_shortest_path(start, end)
    print('Shortest path: ' + shortest_path + ' with length = ' + str(costs[end]))


graph1 = {
    'start': {
        'a': 6,
        'b': 2},
    'a': {
        'fin': 1},
    'b': {
        'a': 3,
        'fin': 5},
    'fin': {}
}


graph3 = {
    'start': {
        'a': 10},
    'a': {
        'c': 20},
    'b': {
        'a': 1},
    'c': {
        'b': 1,
        'fin': 30},
    'fin': {}
}

start = 'start'
end = 'fin'
djikstra(graph3, start, end)


