import time
import numpy as np
start = time.time()
i = open('11_test.txt').read()

space = [[x for x in y] for y in i.split('\n')]
space = np.asarray(space)

def inter(grid):
    new = []
    for x in grid:
        if not '#' in x: new.append(x)
        new.append(x)
    new = np.asarray(new)
    return new

space = inter(space)
space = inter(space.T).T

m = np.where(space=='#')

total = 0
for x in range(len(m[0])):
    r1, c1 = m[0][x], m[1][x]
    for y in range(x):
        r2, c2 = m[0][y], m[1][y]
        total += abs(r1-r2) + abs(c1-c2)
print(total)

print("--- %s ms ---" % ((time.time() - start)*1000))