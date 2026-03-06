import time
start_time = time.time()

sec = open('22.txt').read()
secrets = [int(x) for x in sec.split("\n")]

diffs = {}

def nextSecret(s):
    s = s ^ (s*64)
    s = s % 16777216

    s = s ^ int(s/32)
    s = s % 16777216

    s = s ^ (s*2048)
    s = s % 16777216

    return s

def updateFromSecrets(secrets):
    for x in diffs:
        diffs[x][1] = True

    for s in range(len(secrets)-4):
        a = []
        for n in range(4):
            a.append(secrets[s+n+1]-secrets[s+n])

        if tuple(a) in diffs and diffs[tuple(a)][1]:
            diffs[tuple(a)][0] += secrets[s+4]
            diffs[tuple(a)][1] = False
        elif tuple(a) not in diffs:
            diffs[tuple(a)] = [secrets[s+4],False]

numSecrets = 2000

for secret in secrets:
    s = []
    for x in range(numSecrets):
        s.append(secret%10)
        secret = nextSecret(secret)

    updateFromSecrets(s)

m = max(diffs, key=diffs.get)
print(m, diffs[m][0])

print("--- %s seconds ---" % (time.time() - start_time))