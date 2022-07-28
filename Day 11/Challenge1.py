def flash(octupi, x, y):
    octupi[x][y] = 0
    overFlow = []
    if x != 0: 
        if octupi[x-1][y] != 0:
            octupi[x-1][y] += 1
            if octupi[x-1][y] > 9: 
                overFlow.append([x-1, y])
        if y != 0: 
            if octupi[x-1][y-1] != 0:
                octupi[x-1][y-1] += 1
                if octupi[x-1][y-1] > 9:
                    overFlow.append([x-1, y-1])
        if y != len(octupi[0]) - 1:
            if octupi[x-1][y+1] != 0:
                octupi[x-1][y+1] += 1
                if octupi[x-1][y+1] > 9:
                    overFlow.append([x-1, y+1])
    if x != len(octupi) - 1:
        if octupi[x+1][y] != 0:
            octupi[x+1][y] += 1
            if octupi[x+1][y] > 9:
                overFlow.append([x+1, y])
        if y != 0:
            if octupi[x+1][y-1] != 0:
                octupi[x+1][y-1] += 1
                if octupi[x+1][y-1] > 9:
                    overFlow.append([x+1, y-1])
        if y != len(octupi[0]) - 1:
            if octupi[x+1][y+1] != 0:
                octupi[x+1][y+1] += 1
                if octupi[x+1][y+1] > 9:
                    overFlow.append([x+1, y+1])
    if y != 0:
        if octupi[x][y-1] != 0:
            octupi[x][y-1] += 1
            if octupi[x][y-1] > 9:
                overFlow.append([x, y-1])
    if y != len(octupi[0]) - 1:
        if octupi[x][y+1] != 0:
            octupi[x][y+1] += 1
            if octupi[x][y+1] > 9:
                overFlow.append([x, y+1])
    
    return overFlow, octupi
    

def checkFlash(octupi):
    overFlow = []
    for x in range(len(octupi)):
        for y in range(len(octupi[x])):
            if octupi[x][y] > 9:
                overFlow.append([x, y])
    return overFlow

def increment(octupi):
    for x in range(len(octupi)):
        for y in range(len(octupi[x])):
            octupi[x][y] = octupi[x][y] + 1
    return octupi

with open("input.txt") as txtFile:
    data = txtFile.readlines()

data = [[int(x) for x in a.strip("\n")] for a in data]
flashed = []
flashes = []
counter = 0

for i in range(100):
    data = increment(data)
    flashes = checkFlash(data)
    while(len(flashes) != 0):
        while(flashes[0] in flashed):
            flashes.pop(0)
            if len(flashes) == 0:
                break
        if len(flashes) == 0:
                break
        x = flashes[0][0]
        y = flashes[0][1]
        temp, data = flash(data, x, y)
        counter += 1
        flashed.append(flashes[0])
        flashes.pop(0)
        flashes = flashes + temp
    flashed = []

print(counter)