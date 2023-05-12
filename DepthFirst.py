print("\n\n------------------------------------")
print("\tDepth First Search")
print("------------------------------------")
print("\tM. Sanaullah (RC-02)\n\n")

graph = {
    'S': ['A', 'C'],
    'A': ['F', 'B'],
    'C': ['D', 'G2'],
    'F': ['G2', 'G1'],
    'B': ['G1', 'D'],
    'D': ['G1'],
    'G2': [],
    'G1': []
}

visited = []
queue = ['S']
childnode = []
childnode2 = []


def dfs(graph, visited, goal):
    m = queue.pop(0)
    visited.append(m)
    print(m, end=" ")

    if m == goal:
        return 1
    else:
        # loop to append children of the current visited node into list named childnode
        for i in graph[m]:
            childnode.append(i)

        # loop to append remaining children at the back of the childnode list to maintain LIFO
        while childnode2:
            childnode.append(childnode2.pop(0))

        # adding the first child node of the visited node into the queue
        queue.append(childnode.pop(0))

        # loop to add the remaining children in the queue to another list named childnode2 to maintain LIFO
        while childnode:
            childnode2.append(childnode.pop(0))


print("\nPath: ")
i = 0
while i != 1:
    i = dfs(graph, visited, 'G1')
print("\n")
