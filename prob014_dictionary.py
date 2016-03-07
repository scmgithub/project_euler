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
#    This is a dictionary-based memoized implementation.  The idea is that once we calculate the sequence
#      length for value x, there is no need to calculate it again.  However, we will need to store and
#      lookup the values, so there may or may not be a speed advantage to this method.
#    Execution time:
#     The execution time varies wildly with respect to the method used to detect existing sequence lengths.
#     The fastest method (see below):
# time python prob014_dictionary.py
# 1 : 1
# .
# .
# .
# 999999 : 259
# 837799 has 525 terms.
# note: top = 1000000

# real  0m16.222s
# user  0m9.980s
# sys 0m2.311s

# top = 1000000
# most = 0
# most_n = 0
# lengths = {}

for x in range(1,top):
  print x,":",
  n = x
  terms = 1
  while n > 1:
    # if n in lengths.keys():  #  Super-slow; not recommended.  user time with top = 100000 (1/10th normal size) was 29m33.907s. 
    # if lengths.has_key(n):   #  Faster;  user time with normal top size was 0m10.688s.  
                               #    has_key has been deprecated in Python 2.7 and removed in 3.0.
    if n in lengths:           #  Fastest.  Recommended.  See timing data above.
      terms += lengths[n]-1
      break;
    else:
      if n % 2 == 0:
        n /= 2
      else:
        n = 3*n + 1
      terms += 1
  lengths[x] = terms
  if terms > most:
    most = terms
    most_n = x
  print terms

print most_n,"has",most,"terms."
print "note: top =",top