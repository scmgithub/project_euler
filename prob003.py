# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def isprime(number):
  subfactors = [i for i in range(2, int(math.sqrt(number))+1) if number % i == 0]
  if len(subfactors) > 0:
    return False
  else:
    return True

#candidate = 13195
candidate = 600851475143
largest = 1

factors = [i for i in range(2,int(math.sqrt(candidate))+1) if candidate % i == 0]
  # I use sqrt(candidate) because anything above the sqare root of the candidate can't be a prime factor, though it might be a factor.

# print "Prime factors of %d:" % candidate
# for i in factors:
#   if isprime(i):
#     print i, " ",

for i in factors:
  if isprime(i) and i > largest:
    largest = i

print "The largest prime factor of %d is %d." % (candidate, largest)
