def similiar(strA, strB):
    count = 0
    for i in range(0, len(strA)):
        if strA[i] in strB:
            count += 1
    return count

with open("input.txt") as txtFile:
    data = txtFile.readlines()

data = [[["".join(sorted(y)) for y in a.split(" ")] for a in x.strip("\n").split(" | ")] for x in data]

total = 0

for x in range(len(data)):
    combos = data[x][0]
    numDict = {}
    numDict[1] = [a for a in combos if len(a) == 2][0]
    numDict[4] = [a for a in combos if len(a) == 4][0]
    numDict[7] = [a for a in combos if len(a) == 3][0]
    numDict[8] = [a for a in combos if len(a) == 7][0]
    numDict[6] = [a for a in combos if len(a) == 6 and similiar(a, numDict[7]) != 3][0]
    numDict[3] = [a for a in combos if len(a) == 5 and similiar(a, numDict[7]) == 3][0]
    numDict[9] = [a for a in combos if len(a) == 6 and similiar(a, numDict[3]) == 5][0]
    numDict[0] = [a for a in combos if len(a) == 6 and a != numDict[9] and a != numDict[6]][0]
    numDict[2] = [a for a in combos if len(a) == 5 and similiar(a, numDict[4]) == 2][0]
    numDict[5] = [a for a in combos if len(a) == 5 and similiar(a, numDict[4]) == 3 and a != numDict[3]][0]

    output = ""

    for y in range(len(data[x][1])):
        output = output + str(list(numDict.keys())[list(numDict.values()).index(data[x][1][y])])

    total += int(output)

print(total)