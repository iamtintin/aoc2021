def inBasin(point, basin):
    for x in range(len(basin)):
        if basin[x][0] == point[0] and basin[x][1] == point[1]:
            return True
    return False

def notNine(data, point):
    if data[point[0]][point[1]] == 9: 
        return False
    else:
        return True


def checkAjacent(data, point, basin):
    values = [data[point[0]][point[1]]]
    position = []

    if point[0] != 0:
        tempPoint = [point[0] - 1, point[1]]
        if not inBasin(tempPoint, basin) and notNine(data, tempPoint):
            values.append(data[tempPoint[0]][tempPoint[1]])
            position.append(tempPoint)

    if point[0] != len(data) - 1:
        tempPoint = [point[0] + 1, point[1]]
        if not inBasin(tempPoint, basin) and notNine(data, tempPoint):
            values.append(data[tempPoint[0]][tempPoint[1]])
            position.append(tempPoint)
    
    if point[1] != 0:
        tempPoint = [point[0], point[1] - 1]
        if not inBasin(tempPoint, basin) and notNine(data, tempPoint):
            values.append(data[tempPoint[0]][tempPoint[1]])
            position.append(tempPoint)

    if point[1] != len(data) - 1:
        tempPoint = [point[0], point[1] + 1]
        if not inBasin(tempPoint, basin) and notNine(data, tempPoint):
            values.append(data[tempPoint[0]][tempPoint[1]])
            position.append(tempPoint)

    if max(values) != data[point[0]][point[1]]:
        basin = basin + position
        for x in range (len(position)):
            basin = checkAjacent(data, position[x], basin)

    return basin

with open("input.txt") as txtFile:
    data = txtFile.readlines()

data = [[int(x) for x in a.strip("\n")] for a in data]

lowPoints = []


for x in range(0, len(data)):
    for y in range(0, len(data[0])):
        adjacent = [data[x][y]]
        if x != 0: 
            adjacent.append(data[x-1][y])
        if x != len(data) - 1:
            adjacent.append(data[x+1][y])
        if y != 0:
            adjacent.append(data[x][y-1])
        if y != len(data[0]) - 1:
            adjacent.append(data[x][y+1])

        if min(adjacent) == data[x][y] and adjacent.count(data[x][y]) == 1:
            lowPoints.append([x, y])

basinLengths = []

for i in range(len(lowPoints)):
    low = lowPoints[i]
    basin = [low]
    basin = checkAjacent(data, low, basin)
    basinLengths.append(len(basin))

basinLengths.sort(reverse=True)
print(basinLengths)
print(basinLengths[0] * basinLengths[1] * basinLengths[2])