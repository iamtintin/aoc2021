with open("input.txt") as txtFile:
    data = txtFile.readlines()

data = [[int(x) for x in a.strip("\n")] for a in data]

totalRisk = 0


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
            totalRisk = totalRisk + data[x][y] + 1



print(totalRisk)