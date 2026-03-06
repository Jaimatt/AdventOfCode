import time
start_time = time.time()

sec = open('22.txt').read()
secrets = [int(x) for x in sec.split("\n")]

def nextSecret(s):
    s = s ^ (s*64)
    s = s % 16777216

    s = s ^ int(s/32)
    s = s % 16777216

    s = s ^ (s*2048)
    s = s % 16777216

    return s

numSecrets = 2000

total = 0
for secret in secrets:
    for x in range(numSecrets):
        ns = nextSecret(secret)
        secret = ns
    
    total += secret

print(total)
print("--- %s seconds ---" % (time.time() - start_time))