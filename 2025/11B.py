f = open("11_input.txt")
inp = f.read().split("\n")

# this is our graph
connections = {}

# this is where we'll store values for each node
memos = {}

for x in inp:
    x = x.split(":")
    name = x[0]
    items = x[1].split(" ")[1:]
    connections.update({name:items})

# print(connections)

def traverse(start,end):
    # if reached out, terminate and log 1 path
    if start == end:
        return 1
    # reached end point, this path is invalid
    if start == "out":
        return 0
            
    returnValue = 0

    # otherwise, continue along that path
    for x in connections[start]:
        # print("going to " + x)
        # check if we've already calculated it
        if x in memos:
            returnValue += memos[x]
        else:
            returnValue += traverse(x,end)

    # possibly save the returnValue in memos
    if start not in memos:
        memos.update({start:returnValue})
    
    return returnValue


# through some experimentation, I've deduced it goes to svr -> fft -> dac -> out.
# there can be no paths going dac -> fft because then there'd be loops and paths would be infinite.

# so we'll calculate how many paths exist in stages. First from svr -> fft, then fft -> dac etc.
# because we're doing straight paths from A -> B we can use memoisation (memos) to store the value of each node as we go.
# This makes things ludicrously faster! It's great!!

keyPoints = ["svr","fft","dac","out"]
paths = 1

for x in range(len(keyPoints)-1):
    memos.clear()
    paths = paths * traverse(keyPoints[x],keyPoints[x+1])

print(paths)

# Seriously. Before, I ran it for 3 hours and it barely started. Now, it calculates the 300 trillion number in under a second. It's great!!