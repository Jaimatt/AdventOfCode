f = open('7.txt')
i = f.read().split("\n")
formatted = [[int(line.split(": ")[0]),[int(x) for x in line.split(": ")[1].split(" ")]] for line in i]

def calculate(goal,vals):
    # Base case: end of calculation
    if len(vals) == 1:
        # Return true or false depending on whether it meets the goal
        return goal == vals[0]

    # Recurse case: more calculations
    else:
        # this is just a bit of boolean logic. If either call returns true, it will return true.
        return calculate(goal,[vals[0] + vals[1]] + vals[2:]) or calculate(goal,[vals[0] * vals[1]] + vals[2:])

count = 0
for line in formatted:
    if calculate(line[0],line[1]): count += line[0] 
print(count)

# I'm pretty happy with this code. I feel it's quite elegant.