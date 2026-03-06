z = open('24.txt').read().split('\n\n')

vals = {r.split(': ')[0] : int(r.split(': ')[1]) for r in z[0].split('\n')}
rules = [[r.split(' ')[0],r.split(' ')[2],r.split(' ')[1],r.split(' ')[4]] for r in z[1].split('\n')]

nodes = []
for r in rules:
    nodes.append(r[0])
    nodes.append(r[1])
    nodes.append(r[3])

nodes = set(nodes)

for x in nodes:
    print("{id: '"+x+"', label: '"+x+"'},",end="")

print()
print()
print()
print()
print()
print()
print()

for x in rules:
    print("{from: '"+x[0]+"', to: '"+x[3]+"', arrows: 'to', label: '"+x[2]+"' },",end="")
    print("{from: '"+x[1]+"', to: '"+x[3]+"', arrows: 'to', label: '"+x[2]+"' },",end="")



ans = ['z11','rpv','z38','dvq','z31','dmh','ctg','rpb']
ans.sort()
print()
print()
print(','.join(ans))