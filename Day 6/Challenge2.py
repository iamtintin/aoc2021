with open("input.txt") as txtFile:
    data = txtFile.read()

data = [int(a) for a in data.strip("\n").split(",")]

ageDict = {x:data.count(x) for x in data}

for x in range(9):
    if x not in ageDict:
        ageDict[x] = 0

days = 256

for i in range(days):
    tempDict = {}
    for age in range(8, -1, -1):
        if age != 0:
            tempDict[age - 1] = ageDict[age]
        else:
            tempDict[6] = tempDict[6] + ageDict[0]
            tempDict[8] = ageDict[0]
    ageDict = tempDict

print(sum(ageDict.values()))