import time,sys
import numpy as np
start = time.time()
sys.setrecursionlimit(10000)
doc = open('16.txt').read()

grid = [[y for y in x] for x in doc.split("\n")]
energised = [['.' for y in x] for x in doc.split("\n")]

def p():
    for row in range(len(grid)):
        for c in grid[row]:
            print(c,end=" ")

        print("      ",end="")
        for c in energised[row]:
            print(c,end=" ")
        print()

    print()

def dir(dr,dc):
    if dr==-1 and dc==0: return '^'
    if dr==0 and dc==1: return '>'
    if dr==1 and dc==0: return 'v'
    if dr==0 and dc==-1: return '<'


def val(row,col):
    if not (row in range(len(grid)) and col in range(len(grid[0]))): return '#'
    else: return grid[row][col]

def laser(row,col,dr,dc):

    spot = val(row,col)
    if spot == '#': return
    if energised[row][col] == dir(dr,dc): return

    energised[row][col] = dir(dr,dc)

    if (spot == '|' and dr == 0) or (spot == '-' and dc == 0):
        laser(row-dc,col+dr,-dc,dr)
        laser(row+dc,col-dr,dc,-dr)
        return

    if spot in ['\\','/']:
        if (spot == '/') ^ (dc==0): laser(row-dc,col+dr,-dc,dr)
        else: laser(row+dc,col-dr,dc,-dr)
        return

    laser(row+dr,col+dc,dr,dc)

def project(side,i):
    global energised
    energised = [['.' for y in x] for x in doc.split("\n")]
    match side:
        case 0: laser(0,i,1,0)
        case 1: laser(i,len(grid[0])-1,0,-1)
        case 2: laser(len(grid)-1,i,-1,0)
        case 3: laser(i,0,0,1)
    return np.sum(np.asarray(energised) != '.')

m = 0
for s in range(4):
    for i in range(len(grid)):
        m = max(m,project(s,i))
print(m)

print("--- %s ms ---" % ((time.time() - start)*1000))
# OVERTIME: runs in about 2.5 seconds (we aim for no more than 1)