import time
start_time = time.time()

m = open('23.txt').read()
conn = [x.split("-") for x in m.split("\n")]
computers = list(set(sum(conn,[])))

connections = {}
for x in computers: connections[x] = []
for x in conn:
    connections[x[0]].append(x[1])
    connections[x[1]].append(x[0])

def visit(path):
    # return 3-loops w/ t
    if len(path) == 4 and path[0] == path[-1]:
        for x in path:
            if x[0] == 't': return [path]
    
    # terminate iterations too long
    if len(path) > 3:
        return False

    # visit nexts
    loops = []
    for c in connections[path[-1]]:
        if len(path)>1 and c == path[-2]: continue
        result = visit(path + [c])
        if result: loops += result
    return loops

loops = []

for c in computers:
    loops += visit([c])

print(int(len(loops)/6))

print("--- %s seconds ---" % (time.time() - start_time))