# Uniform Cost Search
print("\n\n------------------------------------")
print("\tUniform Cost Search")
print("------------------------------------")

graph = {
    'S': [['A', 5], ['B', 6], ['C', 1]],
    'A': [['G', 3]],
    'B': [['F', 5]],
    'C': [['E', 2]],
    'G': [],
    'F': [],
    'E': [['D', 1]],
    'D': []
}

visited = []
queue = ['S']
childcosts = []
childnode = []
cost = []
totalcost = []
cumulativecost = 0


def ucs(graph, visted, goal):
    global cumulativecost
    m = queue.pop(0)
    visited.append(m)
    print(m, end=" ")
    if (m == goal):
        return 1
    else:
        childcount = 0
        for i in graph[m]:
            childnode.append(i.pop(0))
            childcount = i.pop(0)
            totalcost.append(childcount)
            childcosts.append(childcount+cumulativecost)

        for i in range(0, len(childcosts)):
            for j in range(0, len(childcosts)-1):
                if childcosts[j] > childcosts[j+1]:
                    temp = childcosts[j]
                    childcosts[j] = childcosts[j+1]
                    childcosts[j+1] = temp

                    temp2 = childnode[j]
                    childnode[j] = childnode[j+1]
                    childnode[j+1] = temp2

                    temp3 = totalcost[j]
                    totalcost[j] = totalcost[j+1]
                    totalcost[j+1] = temp3

        node_to_add = childnode.pop(0)
        cumulativecost = childcosts.pop(0)
        cost.append(totalcost.pop(0))
        queue.append(node_to_add)


print("Path: ")
i = 0
while i != 1:
    i = ucs(graph, visited, 'B')

sum = 0
for i in cost:
    sum += i
print("\nPath Cost = ", sum)
