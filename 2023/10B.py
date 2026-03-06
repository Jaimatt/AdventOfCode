import time,sys
start = time.time()
sys.setrecursionlimit(30000)
i = open('10.txt').read()

pipes = [[x for x in y] for y in i.split('\n')]
icons = [['|',[1,0],[-1,0]],['-',[0,1],[0,-1]],['L',[-1,0],[0,1]],['J',[-1,0],[0,-1]],['7',[1,0],[0,-1]],['F',[1,0],[0,1]]]

def p():
    for row in pipes:
        for c in row:
            print(c,end=" ")
        print()
    print()

def findStart():
    for r,row in enumerate(pipes):
        for c,col in enumerate(row):
            if col != "S": continue
            if pipes[r+1][c] in ['|','J','L']: return r+1,c
            if pipes[r-1][c] in ['|','F','7']: return r+1,c
            if pipes[r][c+1] in ['-','7','J']: return r+1,c

def s():
    for r,row in enumerate(pipes):
        for c,col in enumerate(row):
            if col == "S": return [r, c]

def traverse(row,col):
    me = pipes[row][col]
    if me in ['L','J','7','F']: vertices.append([row,col])

    if me in ['S','O','.']: return 0

    pipes[row][col] = 'O'

    routes = []
    for p in icons:
        if me == p[0]:
            routes.append(traverse(row+p[1][0],col+p[1][1]))
            routes.append(traverse(row+p[2][0],col+p[2][1]))
            return max(routes)+1
    return False

sr,sc = findStart()
vertices = []
perimeter = traverse(sr,sc)+1
vertices = [s()] + vertices + [s()]

area = 0
x,y = vertices[0][0],vertices[0][1]

for v in vertices:
    x2,y2 = v[0],v[1]
    area += (x*y2-x2*y)/2
    x,y = x2,y2

print(int(abs(area) - perimeter/2 + 1))

print("--- %s ms ---" % ((time.time() - start)*1000))