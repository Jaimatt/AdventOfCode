# THE FOLLOWING IS JUST INPUT PROCESSING

f = open("10_input.txt")
inp = f.read().split("\n")

machines = []

for x in inp:
    a = x.split(" ")

    b_vector = a[len(a)-1][1:-1].split(",")
    
    for b in range(len(b_vector)):
        b_vector[b] = int(b_vector[b])
        
    A_matrix = []
    for rowNum in range(len(b_vector)):
        row = []
        for button in a[1:-1]:
            # print(rowNum, button)
            row.append(int(str(rowNum) in button))

        A_matrix.append(row)
                

    m = {"A_matrix":A_matrix,"b_vector":b_vector}

    machines.append(m)

# NOW THE SOLVER FUNCTION, FROM PYTHON MIP MODULE

from mip import *

def solveLinear(A,b):
    # solve optimal x where Ax=b

    # first get n the number of buttons
    n = len(A[0])
    
    # then create the model
    m = Model()

    # create the output vector x
    # this is just the vector the model will optimise.
    # It's currently empty, we're just making it the right length, and specifying things like integers.
    x = [ m.add_var(var_type=INTEGER, lb=0) for i in range(n) ]

    # Now we just state the thing we're optimising for, which is the sum of x[i]
    m.objective = xsum(x[i] for i in range(n))

    # Now, state the constraints.
    # It'll be the pos in A (0 or 1) times by x[i]
    # e.g. something like    x[0] + x[3] = 4
    # in above, we need to make sure that the solution space is constrained to those where x[0]+x[3]=4.
    # in this case, '4' would be in the b vector
    for r in range(len(A)):
        m += xsum(A[r][i] * x[i] for i in range(n)) == b[r]

    # run it!
    m.verbose = 0
    m.optimize()

    # return the sum
    solution = [xi.x for xi in x]
    s = 0
    for y in solution:
        s+=y
    return(int(s))

# NOW THE CODE TO LOOP THROUGH ALL MACHINES

sum = 0
for m in machines:
    sum += solveLinear(m["A_matrix"],m["b_vector"])

print(sum)

# holy crap that worked