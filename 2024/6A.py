import time

f = open('6_test.txt')
map = f.read().split("\n")

height = len(map)
width = len(map[0])

mapString = ''.join(map)

map = [[x for x in y] for y in map]   

guard = {
    "X" : 0,
    "Y" : 0,
    "dir" : 0,
}

guard["Y"] = int(mapString.index("^")/width)
guard["X"] = map[guard["Y"]].index("^")


def wallAt(x,y):
    if x not in range(width):
        return False
    if y not in range(height):
        return False
    if map[y][x] == "#":
        return True
    else:
        return False
    
def printMap():
    for y in map:
        for x in y:
            print(x,end="")
        print()
    print()

def dirSymbol(d):
    if d==0: return "^"
    if d==90: return ">"
    if d==180: return "v"
    if d==270: return "<"

while guard["X"] in range(width) and guard["Y"] in range(height):
    # check in front
    going = [0,0]
    match guard["dir"]:
        case 0:
            going = [guard["X"],guard["Y"]-1]
        case 90:
            going = [guard["X"]+1,guard["Y"]]
        case 180:
            going = [guard["X"],guard["Y"]+1]
        case 270:
            going = [guard["X"]-1,guard["Y"]]

    # if wall in front, turn
    if wallAt(going[0],going[1]):
        guard["dir"] = (guard["dir"]+90)%360
        map[guard["Y"]][guard["X"]] = dirSymbol(guard["dir"])
    else:
        map[guard["Y"]][guard["X"]] = dirSymbol(guard["dir"])
        guard["X"] = going[0]
        guard["Y"] = going[1]

    printMap()
    input()

# now count the squares

counter = 0
for y in map:
    for x in y:
        if x == "@":
            counter += 1

printMap()
print(counter)