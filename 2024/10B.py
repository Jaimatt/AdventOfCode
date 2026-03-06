m = open('10.txt').read()

matrix = [[int(x) for x in y] for y in m.split("\n")]

def val(y,x):
    if not (x in range(len(matrix[0])) and y in range(len(matrix))):
        return 10
    return matrix[y][x]

def trailHead(y,x):
    me = matrix[y][x]
    # base
    if me == 9:
        return 1
    
    # recurse
    routes = 0
    if val(y+1,x) == me + 1: routes += trailHead(y+1,x)
    if val(y-1,x) == me + 1: routes += trailHead(y-1,x)
    if val(y,x+1) == me + 1: routes += trailHead(y,x+1)
    if val(y,x-1) == me + 1: routes += trailHead(y,x-1)
    return routes

def p():
    for row in matrix:
        for c in row:
            print(c,end="")
        print()
    print()

def countPeaks():
    return sum([row.count("T") for row in matrix])

totalscore = 0
for j,y in enumerate(matrix):
    for i,x in enumerate(y):
        if matrix[j][i] == 0:
            totalscore += trailHead(j,i)
            matrix = [[int(x) for x in y] for y in m.split("\n")]
print(totalscore)