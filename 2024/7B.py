f = open('7.txt')
i = f.read().split("\n")
formatted = [[int(line.split(": ")[0]),[int(x) for x in line.split(": ")[1].split(" ")]] for line in i]

# The only change in 7B is a new operator, which is trivial as I only need a third recursive call

def calculate(goal,vals):
    # Base case: end of calculation
    if len(vals) == 1:
        # Return true or false depending on whether it meets the goal
        return goal == vals[0]

    # Recurse case: more calculations
    else:
        # this is just a bit of boolean logic. If any call returns true, it will return true.
        add = calculate(goal,[vals[0] + vals[1]] + vals[2:])
        mul = calculate(goal,[vals[0] * vals[1]] + vals[2:])
        concat = calculate(goal,[ int(str(vals[0])+str(vals[1]))] + vals[2:])
        return add or mul or concat

count = 0
for line in formatted:
    if calculate(line[0],line[1]): count += line[0] 
print(count)