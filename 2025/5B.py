f = open("5_test.txt")
data = f.read().split("\n\n")

ranges = data[0].split("\n")

print("calculating...")

for x in range(len(ranges)):
    ranges[x] = ranges[x].split("-")
    ranges[x][0] = int(ranges[x][0])
    ranges[x][1] = int(ranges[x][1])

valid = []
num = 0

for r in ranges:
    for x in range(r[0],r[1]+1):
        if x not in valid:
            valid.append(x)
    print(str(num+1) + " out of " + str(len(ranges)) + " completed.")
    num += 1


print(valid)
print(len(valid))
input()


# this did not work as it takes too much time, which should have been obvious!