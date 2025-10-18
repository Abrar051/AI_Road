from queue import PriorityQueue


# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
#
#
# heuristic = {
#     'A': 10,
#     'B': 8,
#     'C': 5,
#     'D': 7,
#     'E': 3,
#     'F': 0  # Goal
# }

graph = {
     'A': ['B', 'C'],
     'B': ['D'],       # Dead end path (looks good but fails)
     'C': ['E'],       # Correct path
     'D': [],
     'E': []
 }

heuristic = {
     'A': 10,
     'B': 5,   # Looks better (smaller)
     'C': 6,
     'D': 4,   # Dead end — but still looks small
     'E': 0    # Goal
}

def find_next_node (node , graph, heuristic , connectingNodes):
    neighbors = graph[node]
    path_value = []
    if graph[node] != []:
        for neighbor in neighbors:
            path_value.append((neighbor , heuristic[neighbor]))
    if graph[node] == []:
        return None
    sorted_data = sorted(path_value, key=lambda x: x[1])
    return path_value[0][0]


def best_first_search(start, goal):
    visited = []
    queue = [(start, [start])]
    print(queue)
    while queue:
        # Sort queue so the node with the smallest heuristic is first
        queue.sort(key=lambda x: heuristic[x[0]])
        print('Queue ' ,queue)
        current, path = queue.pop(0)  # Pick the best (lowest h) node

        print(f"Visiting: {current} | Path so far: {path}")

        if current == goal:
            print("\nGoal reached!")
            return path

        visited.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    print("Goal not reachable.")
    return None


#
# # Run the search
# best_first_search('A', 'F')
#
# pq = PriorityQueue()
# pq.put(heuristic['A'],'A')
# # print(pq.get())

best_first_search('A' , 'E')