# coding=utf-8
# Longest Collatz sequence
# Problem 14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


#  Steve's notes:  Apparently the sequence is defined to stop at 1, though it doesn't say that.
#    This is the straightforward implementation.  Non-memoized.
#    Execution time:
# time python prob014_nomemo.py
# 1 : 1
# .
# .
# .
# 999999 : 259
# 837799 has 525 terms.

# real  1m32.570s
# user  1m9.483s
# sys 0m4.181s

top = 1000000
most = 0
most_n = 0

for x in range(1,top):
  print x,":",
  n = x
  terms = 1
  while n > 1:
    if n % 2 == 0:
      n /= 2
    else:
      n = 3*n + 1
    terms += 1
  if terms > most:
    most = terms
    most_n = x
  print terms

print most_n,"has",most,"terms."