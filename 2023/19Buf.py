import time
start = time.time()
i = open('19_test.txt').read().split('\n\n')

workflows = {x.split('{')[0]:[y for y in x.split('{')[1][:-1].split(',')] for x in i[0].split('\n')}


def accepted(ranges, rules):
    r = rules[0]
    print(r)
    # accept or reject
    if r=='R': return 0
    if r=='A':
        print(ranges)
        return 1

    # other end point
    if ':' not in r: return accepted(ranges,workflows[r])

    cond, dest = tuple(r.split(':'))
    if '>' in cond:
        letter, dilineator = tuple(cond.split('>'))
        return accepted 
        # range may be smth like [1,4000]
        # only allow things above cond.split('>')[1]
        return accepted(part,[dest])
    elif '<' in cond and part[cond.split('<')[0]] < int(cond.split('<')[1]):
        return accepted(part,[dest])

    return accepted(part,rules[1:])

r = [1,4000]
init = {'x':r,'m':r,'a':r,'s':r}
print(accepted(init, workflows['in']))
print(r)

print("--- %s ms ---" % ((time.time() - start)*1000))


# EW fuck this