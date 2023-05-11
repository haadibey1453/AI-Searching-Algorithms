# Task 1 (BFS):
# Open Ended Lab Practice Task 1
print("\n\n------------------------------------")
print("\tBreadth Cost Search")
print("------------------------------------")
print("\tM. Sanaullah (RC-02)\n\n")
graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


print("Path: ")
bfs(visited, graph, 'S')
