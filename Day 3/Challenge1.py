with open("input.txt") as txtFile:
    data = txtFile.readlines()

for i in range(0, len(data)):
    data[i] = data[i].strip("\n")

counter = 0
gamma = ""
epsilon = ""

for i in range(0, len(data[0])):
    counter = 0
    for j in range(0, len(data)):
        if data[j][i] == '1':
            counter += 1
    if (counter * 2) > len(data):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma*epsilon)
