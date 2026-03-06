import time
start = time.time()

m = open('17.txt').read().split("\n")

program = [int(x) for x in m[4][9:].split(",")]

# Types of operands
def literal(x):
    return x

def combo(x):
    if x in range(4):
        return x
    return register[["A","B","C"][x-4]]

# Operations
def adv(i): #code0
    numerator = register["A"]
    denominator = 2**combo(i)
    ans = int(numerator/denominator)
    register["A"] = ans

def bxl(i): #code1
    register["B"] = register['B'] ^ literal(i)

def bst(i): #code2
    register["B"] = combo(i) % 8

def jnz(i): #code3
    if register["A"] == 0: return
    return literal(i)

def bxc(i): #code4
    register["B"] = register["B"] ^ register["C"]

def out(i): #code5
    return combo(i) % 8

def bdv(i): #code6
    numerator = register["A"]
    denominator = 2**combo(i)
    ans = int(numerator/denominator)
    register["B"] = ans

def cdv(i): #code7
    numerator = register["A"]
    denominator = 2**combo(i)
    ans = int(numerator/denominator)
    register["C"] = ans


def mismatch(output):
    l = min(len(output),len(program))

    return output[:l] != program[:l]

def runProgram():
    output = []
    index = 0
    while index < len(program):
        opcode = program[index]
        operand = program[index+1]

        if opcode == 0: adv(operand)
        elif opcode == 1: bxl(operand)
        elif opcode == 2: bst(operand)
        elif opcode == 3:
            # Loop catching
            if register["A"] == 0: break

            index = jnz(operand) - 2
        elif opcode == 4: bxc(operand)
        elif opcode == 5: 
            output.append(out(operand))

            # Spot errors early
            if mismatch(output) or len(output) > len(program): break
        elif opcode == 6: bdv(operand)
        elif opcode == 7: cdv(operand)
        index += 2
    
    return output

register = {
    "A": int(m[0][12:]),
    "B": int(m[1][12:]),
    "C": int(m[2][12:])
}

x=0
while True:
    x += 1
    register["A"] = x
    register['B'] = 0
    register["C"] = 0

    output = runProgram()

    if output == program:
        print(output)
        break

    if (x%1000000 == 0): print(x/1000000, time.time() - start)

print("--- %s seconds ---" % (time.time() - start))