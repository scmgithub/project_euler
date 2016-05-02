# Lexicographic permutations
# Problem 24

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# digits = ['0','1','2']
digits = ['0','1','2', '3', '4', '5', '6', '7', '8', '9']
# target = 2 
target = 1000000

if type(digits) is list:
  digits = ''.join(digits)

def permute(els):
  if len(els) == 1:
    return els[0]

  perms=[]
  for i, x in enumerate(els):
    for p in permute(els[:i] + els[i+1:]):
      perms.append(x + p)

  return perms

print "The lexicographic permutation number",target,"of the digits",digits,"is",
print permute(digits)[target-1]


import itertools
print "The lexicographic permutation number",target,"of the digits",digits,"is",
print ''.join(list(itertools.permutations(digits))[target-1])
