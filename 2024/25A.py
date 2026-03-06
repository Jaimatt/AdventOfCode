# This seems weirdly easy... :\
# Anyway let's get to work!

import numpy as np

z = open('25.txt').read().split('\n\n')

keys = []
locks = []

for item in z:
    a = [-1,-1,-1,-1,-1]
    for row in item.split('\n'):
        for c,col in enumerate(row):
            a[c] += col == '#'
    
    if item.split('\n')[0] == '#####':
        locks.append(a)
    else:
        keys.append(a)

count = 0
for l in locks:
    for k in keys:
        if max(np.asarray(l) + np.asarray(k)) > 5: continue
        count += 1
print(count)

# THAT WAS IT?? Why was the last puzzle so easy??