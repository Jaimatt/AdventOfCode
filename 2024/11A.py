s = open('11_test.txt').read()

stones = [int(x) for x in s.split(" ")]

def blink():
    newStones = []

    for s in stones:
        if s == 0: newStones += [1]

        elif len(str(s)) % 2 == 0:
            num1 = int(str(s)[:int(len(str(s))/2)])
            num2 = int(str(s)[int(len(str(s))/2):])
            newStones += [num1, num2]

        else: newStones += [s * 2024]

    return newStones

n = 3
print(stones)
for x in range(n):
    stones = blink()
    print(stones)
print(len(stones))