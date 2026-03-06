f = open('9.txt')
m = f.read()

import re

memory = [[int(i/2) if i%2==0 else '.',int(x)] for i,x in enumerate(m)]
string = []
for x in memory:
    string += [str(x[0])] * x[1]

def p(max = 10000):
    for i, x in enumerate(string):
        print(x,end=" ")
        if i >= max-1: break
    print()

def asString():
    out = ""
    for x in string:
        out += x if x == "." else "-"
    return out

def defragment(pushback):
    pbi = string.index(pushback)
    pbl = string.count(pushback)

    gaps = re.findall("\\.{1,}",asString())
    gi = None

    
    for x in gaps:
        if len(x) >= pbl:
            gi = asString().index(x)
            break

    if gi and gi < pbi:
        for i in range(pbl):
            string[gi+i] = pushback
            string[pbi+i] = '.'

def calcAsnwer():
    c = 0
    for i,n in enumerate(string):
        c += 0 if n == '.' else int(n) * i
    return c

# p()

h = int(string[-1])

for x in range(h,0,-1):
    defragment(str(x))
    # p()

print(calcAsnwer())

# the code is verrryyyy slow......