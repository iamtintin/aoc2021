with open("input.txt") as txtFile:
    data = txtFile.readlines()

for i in range(0, len(data)):
    data[i] = data[i].strip("\n")

highCount= 0
o2 = data
co2 = data

for i in range(0, len(data[0])):
    if len(o2) != 1:
        high = [x for x in o2 if x[i] == '1']
        if len(high) * 2 >= len(o2):
            o2 = high
        else:
            o2 = [x for x in o2 if x[i] == '0']
    
    if len(co2) != 1:
        high = [x for x in co2 if x[i] == '1']
        if len(high) * 2 < len(co2):
            co2 = high
        else:
            co2 = [x for x in co2 if x[i] == '0']

    if len(co2) == 1 and len(o2) == 1:
        break
    
o2 = int(o2[0], 2)
co2 = int(co2[0], 2)

print(o2*co2)
