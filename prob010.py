# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math

top = 2000000
sum = 0

def isprime(n):
  if n==1:
    return False
  if n<4:
    return True
  if n % 2 == 0:
    return False
  if n < 9:
    return True
  if n % 3 == 0:
    return False

  div = 5
  while div <= int(math.sqrt(n)):
    if n % div == 0:
      return False
    if n % (div+2) == 0:
      return False
    div += 6
  return True

for i in range(2,top):
  if isprime(i):
    sum += i

print "The sum of all primes less than %d is %d." % (top, sum)
