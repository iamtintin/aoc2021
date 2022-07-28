def fuelCost(positions, optimum):
    fuel = 0
    for x in range(len(positions)):
        fuel += abs(positions[x] - optimum)
    return fuel

with open("input.txt") as txtFile:
    data = txtFile.read()

data = [int(a) for a in data.strip("\n").split(",")]

data = sorted(data)

if len(data) % 2 == 1:
    median = data[int(len[data]-1)/2]
    bestFuel = fuelCost(data, median)
else:
    medianLow = data[int(len(data)/2)-1]
    medianHigh = data[int(len(data)/2)]

    fuelCosts = []

    for y in range(medianLow, medianHigh+1):
        fuelCosts.append(fuelCost(data, y))
    
    bestFuel = min(fuelCosts)

print(bestFuel)

    
    