from collections import deque


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

mango_sellers = ['barbara']


def find_mango_seller(graph, start_node, mango_sellers):
    search_queue = deque()
    search_queue.append((start_node, 0))
    searched = []

    while search_queue:
        person, degree = search_queue.popleft()
        if person not in searched:
            if person in mango_sellers:
                return True, person, degree
            else:
                for neighbor in graph[person]:
                    search_queue.append((neighbor, degree+1))
                searched.append(person)
    return False, None, None


mango_seller_found, person, degree = find_mango_seller(graph, 'you', mango_sellers)
if mango_seller_found:
    print(f'Closest mango seller is {person.capitalize()} with {degree} degrees of separation')
else:
    print('No mango seller found')



