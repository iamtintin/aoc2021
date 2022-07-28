with open("input.txt") as txtFile:
    data = txtFile.readlines()

coords = [x.strip("\n").split(" -> ") for x in data]

for i in range(0, len(coords)):
    coords[i] = [x.split(",") for x in coords[i]]
    for x in range(len(coords[0])):
        coords[i][x] = [int(z) for z in coords[i][x]]

points = []

for i in range(len(coords)):
    coord = coords[i]
    if (coord[0][0] == coord[1][0]):

        diff = abs(coord[1][1] - coord[0][1])

        if coord[0][1] < coord[1][1]:
            step = 1
        else:
            step = -1
        
        for x in range(0, diff+1):
            points.append([coord[0][0], coord[0][1] + step * x])

    elif (coord[0][1] == coord[1][1]):

        diff = abs(coord[1][0] - coord[0][0])

        if coord[0][0] < coord[1][0]:
            step = 1
        else:
            step = -1
        
        for x in range(0, diff+1):
            points.append([coord[0][0] + step * x, coord[0][1]])
    
pointsDict = {}

for i in range(0, len(points)):
    pointStr = ','.join([str(a) for a in points[i]])
    if pointStr in pointsDict:
        pointsDict[pointStr] = pointsDict[pointStr] + 1
    else: 
        pointsDict[pointStr] = 1

#pointDict = {x:points.count(x) for x in set(points)}
overlap = [v for k,v in pointsDict.items() if v >= 2]
print(len(overlap))

        


