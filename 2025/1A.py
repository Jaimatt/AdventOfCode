num = 50
zeroes = 0

print(num)

f = open("1_input.txt")
actions = f.read().split("\n")

for x in actions:
    direction = x[0]
    distance = int(x[1:])

    print("Going: " + direction)
    print("Dist.: " + str(distance))

    if direction == "L":
        distance = -1 * distance
    
    num = num + distance

    num = num%100

    print(num)

    if num == 0:
        zeroes = zeroes + 1

print(zeroes)