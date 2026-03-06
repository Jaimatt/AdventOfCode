f = open("11_input.txt")
inp = f.read().split("\n")

connections = {}

for x in inp:
    x = x.split(":")
    name = x[0]
    items = x[1].split(" ")[1:]
    connections.update({name:items})

print(connections)

global outs
outs = 0

def traverse(fromNode):
    global outs
    # if reached out, terminate
    if fromNode == "out":
        outs += 1
        return
    # otherwise, continue along that path
    for x in connections[fromNode]:
        print("going to " + x)
        traverse(x)

    # Apparently there are no loops? Which removed all the challenge which is kinda nice.

traverse("you")
print(outs)