from pprint import pprint


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['peggy', 'anuj']
graph['peggy'] = []
graph['anuj'] = []
graph['claire'] = ['thom', 'jonny']
graph['thom'] = []
graph['jonny'] =['barbara']
graph['barbara'] = []

mango_sellers = ['mark']


def find_mango_seller(graph):
    queue = [('you', 0)]
    for item, degree in queue:
        if item in mango_sellers:
            return f'Closest mango seller is {item}, with {degree} degrees of separation'
        else:
            neighbors = graph[item]
            for neighbor in neighbors:
                queue.append((neighbor, degree + 1))

    return 'No mango seller found'


print(find_mango_seller(graph))