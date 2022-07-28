def paths(fromNode, data, workingGraph):
    connections = []
    for i in range(len(data)):
        if data[i][0] == fromNode:
            if not data[i][1].isupper() and data[i][1] not in workingGraph:
                connections.append(data[i][1])
            if data[i][1].isupper():
                connections.append(data[i][1])
        elif data[i][1] == fromNode:
            if not data[i][0].isupper() and data[i][0] not in workingGraph:
                connections.append(data[i][0])
            if data[i][0].isupper():
                connections.append(data[i][0])
    return connections

def allPaths(fromNode, toNode, graph, workingRoute):

    if fromNode == toNode:
        return [workingRoute]

    options = paths(fromNode, data, workingRoute)

    validRoutes = []

    for option in options:
        tempWorkingRoute = workingRoute.copy()
        tempWorkingRoute.append(option)
        route = allPaths(option, toNode, graph, tempWorkingRoute)
        if route != None:
            validRoutes = validRoutes + (route)
        
    return validRoutes

with open("input.txt") as txtFile:
    data = txtFile.readlines()

data = [a.strip("\n").split("-") for a in data]

all = allPaths("start", "end", data, ["start"])

print(len(all))