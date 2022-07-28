with open("input.txt") as txtFile:
    data = txtFile.read()

data = [int(a) for a in data.strip("\n").split(",")]

days = 80

for i in range(days):
    for x in range(len(data)):
        if (data[x] != 0):
            data[x] = data[x] - 1
        else:
            data[x] = 6
            data.append(8)

print(len(data))