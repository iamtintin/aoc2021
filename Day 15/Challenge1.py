import sys

def getAdjacent(maze, current):
    children = []
    for position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        node = (current[0] + position[0], current[1] + position[1])

        if node[0] > (len(maze) - 1) or node[0] < 0 or node[1] > (len(maze[0]) - 1) or node[1] < 0:
            continue

        children.append(node)
    return children

def dijkstra(graph):
    unvisitedNodes = [[",".join([str(a),str(b)]) for b in range(len(graph[0]))] for a in range(len(graph))]
    unvisitedNodes = [item for sublist in unvisitedNodes for item in sublist]
    shortest_path = {}
    previous_nodes = {}

    max_value = sys.maxsize
    for node in unvisitedNodes:
        shortest_path[node] = max_value
    shortest_path["0,0"] = 0

    while unvisitedNodes:
        current_min_node = None
        for node in unvisitedNodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        
        neighbors = getAdjacent(graph, [int(a) for a in current_min_node.split(",")])
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph[neighbor[0]][neighbor[1]]
            neighborKey = ",".join([str(a) for a in neighbor])
            if tentative_value < shortest_path[neighborKey]:
                shortest_path[neighborKey] = tentative_value
                previous_nodes[neighborKey] = current_min_node

        unvisitedNodes.remove(current_min_node)
        
    end = str(len(graph) - 1) + "," + str(len(graph[0]) - 1)
    return shortest_path[end]

def main():

    with open("input.txt") as txtFile:
        data = txtFile.readlines()

    data = [[int(y) for y in x.strip("\n")] for x in data]

    print(dijkstra(data))

if __name__ == '__main__':
    main()