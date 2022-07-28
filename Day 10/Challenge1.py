with open("input.txt") as txtFile:
    data = txtFile.readlines()

data = [x.strip("\n") for x in data]

lookUp = {")": 3, "}": 1197, "]": 57, ">": 25137}
total = 0

for i in range(len(data)):
    corresponding = {"(": ")", "{": "}", "[": "]", "<": ">"}
    expectedBuffer = []
    for a in range(len(data[i])):
        current = data[i][a]
        if current in corresponding:
            expectedBuffer.append(corresponding[current])
        else:
            if expectedBuffer[len(expectedBuffer)-1] != current:
                errorVal = lookUp[current]
                total += errorVal
                break
            else:
                expectedBuffer.pop(len(expectedBuffer) - 1)

print(total)
