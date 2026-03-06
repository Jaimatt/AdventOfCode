import time
start_time = time.time()

m = open('23.txt').read()

conn = [x.split("-") for x in m.split("\n")]
computers = list(set(sum(conn,[])))
connections = {}
for x in computers: connections[x] = set([])
for x in conn:
    connections[x[0]].add(x[1])
    connections[x[1]].add(x[0])

placed = {}
for x in computers: placed[x] = False

longestComponent = set([])

for i, c in enumerate(computers):
    # skip if already in a placement
    if placed[c]: continue

    # place the computer with id i+1
    placed[c] = i+1

    component = set([c])

    # for everything connected to c:
    for cJoin in connections[c]:
        # if its connected to everything in component, add it to component
        if component <= connections[cJoin]:
            component.add(cJoin)
            placed[cJoin] = i+1

    if len(component) > len(longestComponent):
        longestComponent = component

f = list(longestComponent)
f.sort()
print(','.join(f))

print("--- %s seconds ---" % (time.time() - start_time))

# A part-2 in the 20s in less than 0.1 second? Oh YEAH!!
# The trick- use the right data structure (I used sets!)