with open("input.txt") as txtFile:
    data = txtFile.readlines()

data = [[["".join(sorted(y)) for y in a.split(" ")] for a in x.strip("\n").split(" | ")] for x in data]

counter = 0

for x in range(len(data)):
    combos = data[x][0]
    one = [a for a in combos if len(a) == 2][0]
    four = [a for a in combos if len(a) == 4][0]
    seven = [a for a in combos if len(a) == 3][0]
    eight = [a for a in combos if len(a) == 7][0]
    for y in range(len(data[x][1])):
        if data[x][1][y] == one or data[x][1][y] == four or data[x][1][y] == seven or data[x][1][y] == eight:
            counter += 1

print(counter)