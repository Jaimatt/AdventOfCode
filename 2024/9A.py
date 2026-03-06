f = open('9.txt')
m = f.read()

import re

memory = [[int(i/2) if i%2==0 else '.',int(x)] for i,x in enumerate(m)]
string = []
for x in memory:
    string += [str(x[0])] * x[1]

def p():
    for x in string:
        print(x,end=" ")
    print()

def swapSpots():
    dit = string.index('.')

    ln = -1
    while string[ln] == ".":
        ln -= 1

    string[dit], string[ln] = string[ln], string[dit]

def checkDone():
    n = len(re.findall("[0-9]{1,}",''.join(string)))
    return n == 1

def calcAsnwer():
    c = 0
    for i,n in enumerate(string):
        if n == '.':
            return c
        c+= int(n) * i

p()
while not checkDone():
    swapSpots()
    p()

print(calcAsnwer())