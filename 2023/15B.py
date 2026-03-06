import time
start = time.time()
i = open('15.txt').read()

def hash(s):
    out = 0
    for x in s:
        out += ord(x)
        out *= 17
    return out%256

def insert(key,val):
    if hash(key) in hashmap:
        for i, lens in enumerate(hashmap[hash(key)]):
            if lens[0] == key:
                hashmap[hash(key)][i][1] = val
                return
        hashmap[hash(key)].append([key,val])
    else: hashmap[hash(key)] = [[key,val]]

def remove(key):
    if hash(key) not in hashmap: return
    for i, lens in enumerate(hashmap[hash(key)]):
        if lens[0] == key:
            hashmap[hash(key)].pop(i)
            return

hashmap = {}
for x in i.split(","):
    if '=' in x: insert(x.split('=')[0],int(x.split('=')[1]))       
    if '-' in x: remove(x[:-1])

end = 0
for box in hashmap:
    for i, pair in enumerate(hashmap[box]):
        end += (box+1) * (i+1) * pair[1]
print(end)

print("--- %s ms ---" % ((time.time() - start)*1000))