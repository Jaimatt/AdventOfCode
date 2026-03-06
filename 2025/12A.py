f = open("12_input.txt")
inp = f.read().split("\n\n")

print(inp)

boxes = []

regions = []

for x in range(len(inp)-1):
    boxes.append(inp[x][3:])

temp = inp[len(inp)-1].split("\n")

for x in temp:
    y = x.split(": ")
    region = {
        "dim":y[0].split("x"),
        "dist":y[1].split(" "),
        "possible":1
    }
    for y in range(len(region["dim"])):
        region["dim"][y] = int(region["dim"][y])
    for y in range(len(region["dist"])):
        region["dist"][y] = int(region["dist"][y])
    regions.append(region)

print(boxes)
print(regions)

# super trivial way to establish an upper bound:
for r in regions:
    size = r["dim"][0] * r["dim"][1]

    # just figure out the theoretical volume it would require, 
    volume = 0
    for q in range(len(boxes)):
        boxSize = boxes[q].count("#")

        volume += boxSize * r["dist"][q]

    # print(size,volume)
    if volume <= size:
        print("theoretically could fit")
    else:
        print("impossible!")
        r["possible"] = 0


# count possibles
p=0
for r in regions:
    p += r["possible"]
print(p)