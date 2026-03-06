f = open("9_input.txt")
points = f.read().split("\n")

for x in range(len(points)):
    points[x] = points[x].split(",")
    points[x][0] = int(points[x][0])
    points[x][1] = int(points[x][1])

# define size calculation function
def rectSize(pts):
    point1 = points[pts[0]] #2,5
    point2 = points[pts[1]] #11,1
    print(point1, point2)

    size = (abs(point1[0] - point2[0]) +1) * (abs(point1[1] - point2[1]) + 1)

    return size


# create connections

connections = []

for x in range(len(points)):
    for y in range(x):
        connections.append([x,y])

connections.sort(key=rectSize, reverse=True)

print(rectSize(connections[0]))
print((connections[0]))