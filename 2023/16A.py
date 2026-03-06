import time,sys
import numpy as np
start = time.time()
sys.setrecursionlimit(3000)
i = open('16.txt').read()

grid = [[y for y in x] for x in i.split("\n")]
energised = [['.' for y in x] for x in i.split("\n")]

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

laser(0,0,0,1)
# p()
print(np.sum(np.asarray(energised) != '.'))

print("--- %s ms ---" % ((time.time() - start)*1000))