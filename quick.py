#  Scratch file for code snippets and random tests.

import math
# for x in [2,5,10,48,49]:
#   print x, math.sqrt(x), math.floor(math.sqrt(x))


# targ_divisors = 6
# triangle = 0
# addend = 1
# divisors = 0

# while divisors <= targ_divisors:
#   triangle += addend
#   print "triangle: ",triangle," ",
#   addend += 1

#   divisors = 0
#   for x in range(1,int(math.floor(math.sqrt(triangle))+1)):
#     if triangle % x == 0:
#       divisors += 1
#   divisors *= 2
#   print divisors,"divisors"

# print math.pow(2,15)
# print math.pow(2,50)
def isprime(n):
  if n<=1:
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

print "197", isprime(197)
print "179", isprime(179)
print "917", isprime(917)