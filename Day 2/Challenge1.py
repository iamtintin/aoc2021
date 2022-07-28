with open("input.txt") as txtFile:
    cmds = txtFile.readlines()

horizontal = 0
depth = 0

for i in range(0, len(cmds)):
    instruction = cmds[i].split(" ")
    if instruction[0] == "forward":
        horizontal += int(instruction[1])
    elif instruction[0]  == "up":
        depth -= int(instruction[1]) 
    else:
        depth += int(instruction[1])

print(depth * horizontal)