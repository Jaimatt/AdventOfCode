f = open('4.txt')
wordsearch = f.read()

cols = len(wordsearch.split('\n')[0])
wordsearch = wordsearch.replace('\n','n')

import re

# strategy: look for all X shaped things. Then check them individually for:
#  - ensure two Ms and two Ss
#  - ensure appropriate line breaks

regex = '(?=([SM].[SM].{'+str(cols-1)+'}A.{'+str(cols-1)+'}[SM].[SM]))'
list = re.findall(regex,wordsearch)


# Now just validate the results
counter = 0
for x in list:
    # check for right number of lines
    if not x.count("n") == 2:
        print("line error!")
        continue

    # key points
    print(x[0], x[2], x[2+cols], x[2+cols+cols], x[4+cols+cols])
    kp = [x[0], x[2], x[2+cols+cols], x[4+cols+cols]]

    # check for right number of Ms
    if not kp.count("M") == 2:
        print('count error')
        continue

    # check for each MAS ending in distinct letters
    if kp[0] == kp[3] or kp[1] == kp[2]:
        print('match error')
        continue

    counter += 1

print(counter)