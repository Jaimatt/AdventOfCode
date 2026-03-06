m = open('15.txt').read().split("\n\n")

warehouse = [[x for x in row] for row in m[0].split("\n")]
instructions = [i for i in ''.join(m[1].split("\n"))]

def p():
    for row in warehouse:
        for c in row:
            print(c,end="")
        print()
    print()

def robotPos():
    for r, row in enumerate(warehouse):
        for c, col in enumerate(row):
            if col == "@": return r,c

def score():
    count = 0
    for r, row in enumerate(warehouse):
        for c, col in enumerate(row):
            if col == "O":
                count += 100 * r + c
    return count

def moveItem(row, col, dir):
    # Specify the direction we're going
    x,y = 0,0
    if dir == "v": y=1
    if dir == "^": y=-1
    if dir == "<": x=-1
    if dir == ">": x=1

    # if we're going to a wall, cease work
    if warehouse[row + y][col + x] == '#':
        return
    
    # if it's a box, attempt to push it
    if warehouse[row + y][col + x] == 'O':
        moveItem(row + y, col + x, dir)

    # if there's empty space, push yourself into it
    if warehouse[row + y][col + x] == '.':
        warehouse[row + y][col + x], warehouse[row][col] = warehouse[row][col], warehouse[row + y][col + x]

for i in instructions:
    r,c = robotPos()
    moveItem(r,c,i)

print(score())