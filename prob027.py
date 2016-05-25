# coding=utf-8
# Quadratic primes
# Problem 27

# Euler discovered the remarkable quadratic formula:

# n² + n + 41

# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

#     n² + an + b, where |a| < 1000 and |b| < 1000

#     where |n| is the modulus/absolute value of n
#     e.g. |11| = 11 and |−4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

# Interesting discussion (about Python and primeness) here:
#   http://codereview.stackexchange.com/questions/47055/project-euler-27-quadratic-primes

import primeness   # My own module dealing with primes

limit = 1000
max_string = 0
prod_of_max = 0

for a in range(-limit+1,limit):
  for b in range (1,limit):
    # Since we start at n=0, 0^2+a*0+b = b implies that b must be prime.
    #  Also, b must be positive.
    if not primeness.isprime(b) or b < 1:
      continue
    n = 0
    while primeness.isprime(n*n+a*n+b):
      n+=1
    if n > max_string:
      max_string = n
      prod_of_max = a*b
      print a,"*",b,"=",prod_of_max,"at string length",n

print prod_of_max
