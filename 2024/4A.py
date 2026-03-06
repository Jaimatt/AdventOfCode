f = open('4.txt')
wordsearch = f.read()

cols = len(wordsearch.split('\n')[0])

print(wordsearch)
print(cols)

wordsearch = wordsearch.replace('\n','n')

print(wordsearch)

# perform 8 RegExs, one for each direction

import re

found = 0

# horizontal
found += len(re.findall('(?=XMAS)',wordsearch))
found += len(re.findall('(?=SAMX)',wordsearch))

# vertical
found += len(re.findall('(?=X.{'+str(cols)+'}M.{'+str(cols)+'}A.{'+str(cols)+'}S)',wordsearch))
found += len(re.findall('(?=S.{'+str(cols)+'}A.{'+str(cols)+'}M.{'+str(cols)+'}X)',wordsearch))

# forward diagonal
found += len(re.findall('(?=X.{'+str(cols+1)+'}M.{'+str(cols+1)+'}A.{'+str(cols+1)+'}S)',wordsearch))
found += len(re.findall('(?=S.{'+str(cols+1)+'}A.{'+str(cols+1)+'}M.{'+str(cols+1)+'}X)',wordsearch))

# backward diagonal
found += len(re.findall('(?=X.{'+str(cols-1)+'}M.{'+str(cols-1)+'}A.{'+str(cols-1)+'}S)',wordsearch))
found += len(re.findall('(?=S.{'+str(cols-1)+'}A.{'+str(cols-1)+'}M.{'+str(cols-1)+'}X)',wordsearch))

print(found)


# It worked!!
# I thought I may have to debug to avoid wrap-around, but no. Luckily that didn't transpire