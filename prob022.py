# coding=utf-8
# Names scores
# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import re

namefile = "prob022_names.txt"
idx = 1
total_score = 0

with open(namefile) as f:
  for line in f:
    names = filter(None, re.split('[" ,]+', line))

names.sort()

for name in names:
  namescore = 0
  for letter in list(name):
    # print letter, ord(letter)-ord('A')+1
    namescore += ord(letter)-ord('A')+1
  namescore *= idx
  total_score += namescore
  idx += 1

print "Total name score is %d." % (total_score)


