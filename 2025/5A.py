f = open("5_input.txt")
data = f.read().split("\n\n")

ranges = data[0].split("\n")
available = data[1].split("\n")

for x in range(len(ranges)):
    ranges[x] = ranges[x].split("-")
    ranges[x][0] = int(ranges[x][0])
    ranges[x][1] = int(ranges[x][1])

for x in range(len(available)):
    available[x] = int(available[x])

# print(ranges)
# print(available)

fresh = 0

for ingredient in available:
    # print("checking:")
    # print(ingredient)
    # loop through and see if it's in a range
    for range in ranges:
        if ingredient < range[0] or ingredient > range[1]:
            # print("out of range")
            # print(range)
            # skip this range, as it is not in the range
            continue
        # otherwise, it's in the range
        # print("within range")
        # print(range)
        fresh += 1
        break

print(fresh)