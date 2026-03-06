m = open('17.txt').read().split("\n")

A,B,C = [int(x[12:]) for x in m[0:3]]
program = [int(x) for x in m[4][9:].split(",")]
index=0
output = ""

# Types of operands

def literal(x):
    return x

def combo(x):
    if x in range(4): 
        return x
    return [A,B,C][x-4]

# Operations

def adv(i): #code0
    global A
    numerator = A
    denominator = 2**combo(i)
    ans = int(numerator/denominator)
    A = ans

def bxl(i): #code1
    global B
    B = B ^ literal(i)

def bst(i): #code2
    global B
    B = combo(i) % 8

def jnz(i): #code3
    global index
    if A == 0: return
    index = literal(i)

def bxc(i): #code4
    global B,C
    B = B ^ C

def out(i): #code5
    global output
    output += str(combo(i) % 8) + ","

def bdv(i): #code6
    global A,B
    numerator = A
    denominator = 2**combo(i)
    ans = int(numerator/denominator)
    B = ans

def cdv(i): #code7
    global A,C
    numerator = A
    denominator = 2**combo(i)
    ans = int(numerator/denominator)
    C = ans

while index < len(program):
    opcode = program[index]
    operand = program[index+1]
    # loop prevention:
    print(A,B,C)
    print(opcode,operand)
    if opcode == 3 and A == 0:
        print()
        print('avoiding loop... breaking')
        break

    if opcode == 0: adv(operand)
    elif opcode == 1: bxl(operand)
    elif opcode == 2: bst(operand)
    elif opcode == 4: bxc(operand)
    elif opcode == 5: out(operand)
    elif opcode == 6: bdv(operand)
    elif opcode == 7: cdv(operand)
    elif opcode == 3:
        jnz(operand)
        continue
    index += 2
print(output)
print(A,B,C)