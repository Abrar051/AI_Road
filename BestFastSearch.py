from queue import PriorityQueue


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 0  # Goal
}


def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))  # (heuristic_value, node)

    while not pq.empty():
        h, node = pq.get()
        print(f"Visiting node: {node}")

        if node == goal:
            print("Goal reached!")
            return True

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

    print("❌ Goal not found.")
    return False


# Run the search
best_first_search('A', 'F')

pq = PriorityQueue()
pq.put(heuristic['A'],'A')
print(pq.get())
