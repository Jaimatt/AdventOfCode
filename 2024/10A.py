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
        matrix[y][x] = 'T'
        return
    
    # recurse
    matrix[y][x] = '#'
    if val(y+1,x) == me + 1: trailHead(y+1,x)
    if val(y-1,x) == me + 1: trailHead(y-1,x)
    if val(y,x+1) == me + 1: trailHead(y,x+1)
    if val(y,x-1) == me + 1: trailHead(y,x-1)


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
            trailHead(j,i)
            totalscore += countPeaks()
            matrix = [[int(x) for x in y] for y in m.split("\n")]

print(totalscore)