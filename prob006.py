# coding=utf-8
# Problem 6

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

max = 100
sum = 0
sumsquares = 0

for i in range(1,max+1):
  sum += i
  sumsquares += i**2

diff = sum**2 - sumsquares

print "The sum of the squares of the first %d natural numbers is %d." % (max, sumsquares)
print "The square of the sum of the first %d natural numbers is %d." % (max, sum**2)
print "The difference is %d." % diff
