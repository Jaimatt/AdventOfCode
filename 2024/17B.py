import time
start = time.time()

# Okay so I copied a strategy from reddit (but modified it for myself). I'm going to try my best to inline-document what I've done.

# First just reverse the program, as we're going through backwards in this code.
p = [2,4,1,5,7,5,0,3,1,6,4,3,5,5,3,0]
p.reverse()

# This is where we'll store all possible answers (later we'll pick the minimum)
ans = []

# This function is recursive.
def fromBack(a,i):
    # Base case
    # If i - the index in program - is at the end, save a as this value works.
    if i == len(p):
        ans.append(a)
        # print("Ans:" + str(a))
        return
        
    # Multiply a, ready for the next digit (because in the actual program a is divided by 8 each loop)
    a = a * 8

    # Recursive case.
    # We're going to try the next 8 values from a, to see if they produce a b whose mod is as desired.
    # We only check the next 8 because a inputs are always mod 8
    for x in range(a,a+8):
        # Calculate b. This is, effectively, what happens each loop through the program.
        # On a pen and paper I've diseminated each program loop into just one equation for quick calculating.
        b = (x%8)^3^int(x/(2**((x%8)^5)))
        # And if b mod 8 is as desired, calculate the next digit from here.
        # x is the value after a that ensures b, so we move forward with this value for a
        if b % 8 == p[i]: fromBack(x,i+1)

# Run, from 0.
fromBack(0,0)

# Then print the answer!
print(min(ans))