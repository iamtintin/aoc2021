with open("input.txt") as txtFile:
    data = txtFile.readlines()

polymer = [a for a in data[0].strip("\n")]

data = [a.strip("\n").split(" -> ") for a in data[2:]]
adjacent = [a[0] for a in data]
addition = [a[1] for a in data]

for i in range(10):
    index = 0 
    while index < len(polymer) - 1:
        key = "".join(polymer[index:index+2])
        if key in adjacent:
            position = adjacent.index(key)
            polymer.insert(index+1, addition[position])
            index += 2
            continue
        index += 1

mostCommon = max(set(polymer), key = polymer.count)
leastCommon = min(set(polymer), key = polymer.count)

mostCommon = polymer.count(mostCommon)
leastCommon = polymer.count(leastCommon)

print(mostCommon - leastCommon)
