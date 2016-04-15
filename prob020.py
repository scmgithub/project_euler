# coding=utf-8
# Factorial digit sum
# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import math

num = 100
fact = math.factorial(num)
digit_sum = 0

print "%d! = %d" % (num, fact)

while fact > 0:
  # print "fact is %d" % (fact)
  digit_sum += fact % 10
  fact = int(fact / 10)

print "The digits sum to %d." % (digit_sum)