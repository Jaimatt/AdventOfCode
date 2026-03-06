import time
start = time.time()
i = open('20_test.txt').read()

# code

print("--- %s ms ---" % ((time.time() - start)*1000))