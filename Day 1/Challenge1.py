with open("input.txt") as txtFile:
    depths = txtFile.readlines()

increased = 0

for i in range(1 , len(depths)):
    if int(depths[i]) > int(depths[i-1]):
        increased += 1

print(increased)