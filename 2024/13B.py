m = open('13.txt').read().split("\n\n")

import re

count = 0
for equation in m:
    a = int(re.findall("X\\+[0-9]{1,}",equation)[0][2:])
    c = int(re.findall("Y\\+[0-9]{1,}",equation)[0][2:])
    b = int(re.findall("X\\+[0-9]{1,}",equation)[1][2:])
    d = int(re.findall("Y\\+[0-9]{1,}",equation)[1][2:])
    e = int(re.findall("X\\=[0-9]{1,}",equation)[0][2:]) + 10000000000000
    f = int(re.findall("Y\\=[0-9]{1,}",equation)[0][2:]) + 10000000000000

    Y = int((a*f-e*c)/(a*d-b*c))
    X = int((e*c-b*c*Y)/(a*c))

    if X*a+Y*b == e and X*c+Y*d == f:
        count += X*3+Y
print(count)