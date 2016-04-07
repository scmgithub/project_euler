# coding=utf-8
# Power digit sum
# Problem 16

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

import math

def sumdigits(big_ian):
  d_sum = 0
  while big_ian > 0:
    d_sum += big_ian % 10
    big_ian /= 10
  return d_sum

base = 2
exponent = 15
print "The sum of the digits of",base,"^",exponent," is",sumdigits(int(math.pow(base,exponent))),"."

exponent = 16
print "The sum of the digits of",base,"^",exponent," is",sumdigits(int(math.pow(base,exponent))),"."

exponent = 1000
print "The sum of the digits of",base,"^",exponent," is",sumdigits(int(math.pow(base,exponent))),"."
