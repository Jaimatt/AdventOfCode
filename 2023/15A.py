import time
start = time.time()
i = open('15.txt').read()

def hash(s):
    out = 0
    for x in s:
        out += ord(x)
        out *= 17
    return out%256

total = sum([hash(x) for x in i.split(",")])
print(total)

print("--- %s ms ---" % ((time.time() - start)*1000))