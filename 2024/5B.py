from functools import cmp_to_key

f = open('5.txt')
inp = f.read().split('\n\n')

inp[0] = inp[0].split('\n')
inp[1] = inp[1].split('\n')

data = {
    "rules" : [inp[0][x].split("|") for x in range(len(inp[0]))],
    "updates" : [inp[1][x].split(",") for x in range(len(inp[1]))]
}

# sorting criterion
def compare(a,b):
    # check every rule
    for x in data["rules"]:
        if not (a in x and b in x):
            continue # the is no rule for these two
        # print(x)
        if x == [a,b]:
            # print("error, fixing...")
            return -1 # correct order
        if x == [b,a]:
            # print("satisfied")
            return 1 # wrong order

# loop through updates
counter = 0
for x in data["updates"]:
    # if it's NOT equal to its sorted form...
    y = sorted(x, key=cmp_to_key(compare))
    if not x == y:
        # ...then count the middle of its sorted form
        counter += int(y[int((len(y)-1)/2)])
print(counter)


# I solved that one in like 20 seconds!
# It was because I'd already written the sorting code, by not only checking each rule in 5A!