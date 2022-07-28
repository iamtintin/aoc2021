def dictRemove(theDict, tempDict, key):
    tempVal = tempDict[key]
    theDict[key] = theDict[key] - tempDict[key]
    return theDict, tempVal

def dictInsert(theDict, key, value):
    if key in theDict:
        theDict[key] = theDict[key] + value
    else:
        theDict[key] = value
    return theDict

def countDict(theDict, ogStart, ogEnd):
    tempList = []
    counter = []
    for key in theDict:
        for i in range(2):
            if key[i] in tempList:
                counter[tempList.index(key[i])] = counter[tempList.index(key[i])] + theDict[key]
            else:
                tempList.append(key[i])
                counter.append(theDict[key])
    for i in range(len(counter)):
        if tempList[i] == ogEnd or tempList[i] == ogStart:
            counter[i] = counter[i] + 1
        counter[i] = counter[i] / 2 
    return counter
        

with open("input.txt") as txtFile:
    data = txtFile.readlines()

polymer = [a for a in data[0].strip("\n")]

data = [a.strip("\n").split(" -> ") for a in data[2:]]
adjacent = [a[0] for a in data]
addition = [a[1] for a in data]

datadict = {}

for i in range(len(polymer) - 1):
    key = "".join(polymer[i:i+2])
    datadict = dictInsert(datadict, key, 1)

for i in range(40):
    tempDict = datadict.copy()
    for key in tempDict:
        if tempDict[key] == 0:
            continue
        if key in adjacent:
            newInsert = addition[adjacent.index(key)]
            datadict, value = dictRemove(datadict, tempDict, key)
            datadict = dictInsert(datadict, key[0] + newInsert, value)
            datadict = dictInsert(datadict, newInsert + key[1], value)

counterList = countDict(datadict, polymer[0], polymer[len(polymer) - 1])

print(int(max(counterList) - min(counterList)))

