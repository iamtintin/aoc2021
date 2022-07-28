def fuelCost(positions, optimum):
    fuel = 0
    for x in range(len(positions)):
        diff = abs(positions[x] - optimum)
        fuel += (diff * (diff + 1) / 2)
    return int(fuel)

with open("input.txt") as txtFile:
    data = txtFile.read()

data = [int(a) for a in data.strip("\n").split(",")]

data = sorted(data)


mean = int(round(sum(data)/len(data))) 

bestFuel = fuelCost(data, mean)

counter = 0

while True:
    tempFuel = fuelCost(data, mean + counter)
    if tempFuel <= bestFuel:
        bestFuel = tempFuel
        counter += 1
    else:
        break

counter = 0

while True:
    tempFuel = fuelCost(data, mean - counter)
    if tempFuel <= bestFuel:
        bestFuel = tempFuel
        counter += 1
    else:
        break


print(bestFuel)

    
    