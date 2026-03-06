import time
start_time = time.time()

z = open('24.txt').read().split('\n\n')

vals = {r.split(': ')[0] : int(r.split(': ')[1]) for r in z[0].split('\n')}
rules = [[r.split(' ')[0],r.split(' ')[2],r.split(' ')[1],r.split(' ')[4]] for r in z[1].split('\n')]

while len(rules) > 0:
    for i, r in enumerate(rules):
        if r[0] not in vals or r[1] not in vals: continue
        match r[2]:
            case 'AND': vals[r[3]] = vals[r[0]] and vals[r[1]]
            case 'OR': vals[r[3]] = vals[r[0]] or vals[r[1]]
            case 'XOR': vals[r[3]] = vals[r[0]] ^ vals[r[1]]
        rules.pop(i)

bi = ''
num = 0
for x in range(len(vals)):
    z = 'z' + str(x)
    if x < 10: z = 'z0' + str(x)

    if z in vals:
        bi = str(vals[z]) + bi
        num += 2**x * vals[z]

print(num)

print("--- %s seconds ---" % (time.time() - start_time))