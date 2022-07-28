with open("input.txt") as txtFile:
    depths = txtFile.readlines()

increased = 0

for i in range(1 , len(depths)-2):
    if int(depths[i+2]) > int(depths[i-1]):
        increased += 1

print(increased)