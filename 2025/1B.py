num = 50
zeroes = 0

print(num)

f = open("1_input.txt")
actions = f.read().split("\n")

for x in actions:
    direction = x[0]
    distance = int(x[1:])

    # print("Going: " + direction)
    # print("Dist.: " + str(distance))

    mull = 1
    if direction == "L":
        mull = -1

    for x in range(distance):
        num = num + mull
        num = num%100
        if num == 0:
            zeroes = zeroes + 1
    
print(zeroes)