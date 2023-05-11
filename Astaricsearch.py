print("\n\n------------------------------------")
print("\tA* Search")
print("------------------------------------")
print("\tM. Sanaullah (RC-02)\n\n")

graph = {
    'S': [['A', 1, 3], ['G', 10, 0]],
    'A': [['C', 1, 2], ['B', 2, 4]],
    'G': [],
    'C': [['G', 4, 0], ['D', 3, 6]],
    'B': [['D', 3, 6]],
    'D': []
}

heuristic_values = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0
}

visited = []
queue = ['S']
childnode = []
childcost = []
childheuristic = []
cost = []
cumulativecost = 0
fncost = []
totalcost = []


def Astaric(graph, visted, goal):
    global cumulativecost
    m = queue.pop(0)
    visited.append(m)
    print(m, end=" ")
    if m == goal:
        return 1
    else:
        # storing child nodes, their costs, and their heuristics separately
        childcount = 0
        for i in graph[m]:
            childnode.append(i.pop(0))
            childcount = i.pop(0)
            totalcost.append(childcount)
            childcost.append(childcount+cumulativecost)
            childheuristic.append(i.pop(0))

        # calculting f(n) = g(n) + h(n)
        fn = []
        for i in range(0, len(childcost)):
            fn.append(childcost[i] + childheuristic[i])

        # bubble sort
        for i in range(0, len(fn)):
            for j in range(0, len(fn)-1):
                if fn[j] > fn[j+1]:
                    temp = fn[j]
                    fn[j] = fn[j+1]
                    fn[j+1] = temp

                    temp2 = childcost[j]
                    childcost[j] = childcost[j+1]
                    childcost[j+1] = temp2

                    temp3 = childnode[j]
                    childnode[j] = childnode[j+1]
                    childnode[j+1] = temp3

                    temp4 = childheuristic[j]
                    childheuristic[j] = childheuristic[j+1]
                    childheuristic[j+1] = temp4

                    temp5 = totalcost[j]
                    totalcost[j] = totalcost[j+1]
                    totalcost[j+1] = temp5

        node_to_add = childnode.pop(0)
        cost_to_add = childcost.pop(0)
        cumulativecost = cost_to_add
        cost.append(totalcost.pop(0))
        childheuristic.pop(0)
        queue.append(node_to_add)


print("Path: ")
i = 0
while i != 1:
    i = Astaric(graph, visited, 'G')

print("\n---------\nCost: ")
cost_sum = 0
for i in cost:
    cost_sum += i
print(cost_sum)
