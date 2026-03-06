f = open("10_input.txt")
inp = f.read().split("\n")

# THE FOLLOWING IS JUST INPUT PROCESSING

machines = []

for x in inp:
    m = {"buttons":[]}
    a = x.split(" ")
    g = a[0][1:-1]
    goal = []

    for k in g:
        if k==".":
            goal.append(0)
        else:
            goal.append(1)

    m.update({"goal":goal})

    for x in a[1:-1]:
        list = x[1:-1].split(',')
        for k in range(len(list)):
            list[k] = int(list[k])
        m["buttons"].append(list)
        

    machines.append(m)

# Now that's done, it's algorithm time!!

print(machines[0])

global optimal
optimal = 1000

def pressButtons(pressed,machine):
    global optimal
    goal = machines[machine]["goal"]
    buttons = machines[machine]["buttons"]

    # immediate end if we're taking longer than the existing optimal solution
    if len(pressed) >= optimal:
        return [0] * len(buttons)
    
    # print(pressed)


    # calculate the state we'll be in now
    state = [0]*len(goal)
    for x in pressed:
        for y in buttons[x]:
            state[y] += 1
            state[y] = state[y]%2

    # return the path, if at the end
    if state == goal:
        if len(pressed) < optimal:
            optimal = len(pressed)
        return pressed

    # now we know what the state is.
    # press a bunch of buttons!

    shortest = [0] * len(buttons)
    for x in range(len(buttons)):
        # if a button has already been pressed, skip
        if x in pressed:
            continue
        
        path = pressButtons(pressed+[x],machine)

        if len(path) < len(shortest):
            shortest = path
        
        # if path is short enough, stop looping!
        if len(path) == len(pressed)+1:
            break

    
    return shortest

    # if the loop to press another button gor nothing, buttonSets is also empty, and the shortest just becomes [0] * len(buttons)
    # the parent recursion will disregard this as it's longer than any other option available (equ to pressing all buttons)
    

totalPresses = 0
for m in range(len(machines)):
# for m in range(1):
    optimal = 1000
    steps = pressButtons([],m)
    totalPresses += len(steps)
    print("Machine " + str(m+1) + " doable in " + str(len(steps)) + " presses.")
    print(str(round(((m+1)/len(machines))*100)) + "% done.")
print("Total " + str(totalPresses))
input()