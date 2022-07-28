with open("input.txt") as txtFile:
    cmds = txtFile.readlines()

horizontal = 0
depth = 0
aim = 0

for i in range(0, len(cmds)):
    instruction = cmds[i].split(" ")
    if instruction[0] == "forward":
        horizontal += int(instruction[1])
        depth += aim * int(instruction[1])
    elif instruction[0]  == "up":
        aim -= int(instruction[1])
    else:
        aim += int(instruction[1])

print(depth * horizontal)