with open("input.txt") as txtFile:
    data = txtFile.readlines()

data = [x.strip("\n") for x in data]

lookUp = {")": 1, "}": 3, "]": 2, ">": 4}
scores = []
error = False

for i in range(len(data)):
    corresponding = {"(": ")", "{": "}", "[": "]", "<": ">"}
    expectedBuffer = []

    for a in range(len(data[i])):
        current = data[i][a]
        if current in corresponding:
            expectedBuffer.append(corresponding[current])
        else:
            if expectedBuffer[len(expectedBuffer)-1] != current:
                error = True
                break
            else:
                expectedBuffer.pop(len(expectedBuffer) - 1)

    if len(expectedBuffer) > 0 and not error:
        score = 0
        for x in reversed(expectedBuffer):
            score *= 5
            score += lookUp[x]
        scores.append(score)
    
    error = False

scores = sorted(scores)
print(scores[int((len(scores) - 1 )/ 2)])
