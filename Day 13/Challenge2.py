def reflect(option, value, cords):
    removal = []
    if option == "x":
        for i in range(len(cords)):
            if cords[i][0] > value:
                xVal = (2 * value) - cords[i][0]
                yVal = cords[i][1]
                if [xVal, yVal] not in cords:
                    cords.append([xVal, yVal])
                removal.append(cords[i])
    else:
        for i in range(len(cords)):
            if cords[i][1] > value:
                xVal = cords[i][0]
                yVal = (2 * value) - cords[i][1]
                if [xVal, yVal] not in cords:
                    cords.append([xVal, yVal])
                removal.append(cords[i])

    cords = removeCords(cords, removal)
    return cords

def removeCords(cods, removeList):
    for cord in removeList:
        cods.remove(cord)
    return cods

def hasNegative(cords):
    for i in range(len(cords)):
        if cords[i][0] < 0 or cords[i][1] < 0:
            return True
    return False

with open("input.txt") as txtFile:
    data = txtFile.readlines()

for i in range(len(data)):
    if data[i] == "\n":
        coords = [[int(x) for x in a.strip("\n").split(",")] for a in data[:i]]
        reflects = [a.strip("\n").split(" ")[2] for a in data[i+1:]]
        break

print(reflects)

for i in range(len(reflects)):
    line, lineVal = reflects[i].split("=")
    coords = reflect(line, int(lineVal), coords)

maxX = 0
maxY = 0

for i in range(len(coords)):
    if coords[i][0] > maxX:
        maxX = coords[i][0]
    if coords[i][1] > maxY:
        maxY = coords[i][1]

for y in range(maxY + 1):
    for x in range(maxX + 1):
        if [x, y] in coords:
            print("#", end="")
        else:
            print(".", end="")
    print()