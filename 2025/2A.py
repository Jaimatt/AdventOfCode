import math

f = open("2_input.txt")
ranges = f.read().split(",")

# PROCESSING
for x in range(len(ranges)):
    ranges[x] = ranges[x].split("-")
    ranges[x][0] = int(ranges[x][0])
    ranges[x][1] = int(ranges[x][1])

# STORAGE
invalids = []

# ALGORITHM
for x in ranges:
    min = x[0]
    max = x[1]
    for y in range(min,max+1):
        string = str(y)
        lenstr = len(string)
        half = math.floor(lenstr/2)
        # remove odd lens
        if lenstr%2 == 1:
            continue
        if string[half:] == string[:half]:
            invalids.append(int(string))

print(invalids)
sum = 0
for x in invalids:
    sum = sum + x
print(sum)