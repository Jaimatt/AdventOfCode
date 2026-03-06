import time
import numpy as np
start = time.time()
i = open('13.txt').read()

grids = [np.asarray([[z for z in y] for y in x.split("\n")]) for x in i.split("\n\n")]

def findMirror(t):
    s = []
    for mirror in range(1,len(t)):
        a = t[:mirror][::-1]
        b = t[mirror:]
        k = min(len(a),len(b))
        if np.sum(a[:k]!=b[:k]) == 0: s.append(mirror)
    return s

total = 0
for g in grids:
    h = findMirror(g)
    v = findMirror(g.T)
    if v: total += v[0]
    else: total += 100*h[0]
print(total)

print("--- %s ms ---" % ((time.time() - start)*1000))