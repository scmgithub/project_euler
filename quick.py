#  Scratch file for code snippets and random tests.

import itertools

for l in range(1,5):
  for x in itertools.permutations([i for i in range(1,l+1)],l):
    print int(''.join(map(str,list(x))))

exit()

for i in itertools.count(5,100):
  print i
  if i > 500:
    break

# exit()

def defaults(x = 5, y = 7):
  print "x is",x
  print "y is",y

defaults(10,20)
defaults(15)
defaults()

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


def ispandigital(n):
  return [str(i) for i in range(1,len(str(n))+1)] == sorted(str(n))

def ispandigitalprime(n):
  return ispandigital(n) and isprime(n)

assert ispandigitalprime(2143)