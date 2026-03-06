s = open('11.txt').read()

stones = [int(x) for x in s.split(" ")]
stones = {}

def addDic(key, num, dic):
    if key in dic:
        dic[key] += num
    else:
        dic[key] = num

for x in s.split(" "):
    stone = int(x)
    addDic(stone,1,stones)

def blink():
    newStones = {}

    for s in stones:
        if s == 0:
            addDic(1,stones[s],newStones)

        elif len(str(s)) % 2 == 0:
            num1 = int(str(s)[:int(len(str(s))/2)])
            num2 = int(str(s)[int(len(str(s))/2):])
            addDic(num1,stones[s],newStones)
            addDic(num2,stones[s],newStones)

        else: 
            addDic(s*2024,stones[s],newStones)

    return newStones

n = 75
for x in range(n): stones = blink()

total = 0
for x in stones: total += stones[x]
print(total)