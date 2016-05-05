# coding=utf-8
# Reciprocal cycles
# Problem 26

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#     1/2 =   0.5
#     1/3 =   0.(3)
#     1/4 =   0.25
#     1/5 =   0.2
#     1/6 =   0.1(6)
#     1/7 =   0.(142857)
#     1/8 =   0.125
#     1/9 =   0.(1)
#     1/10  =   0.1 

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


#  This one is very number-theory heavy, even to the point that it is sort of "unfair"
#   to expect someone without a background in number theory to be able to solve it efficiently.
#
# See these pages for a ton of discussion:
# https://projecteuler.net/problem=26
# https://oeis.org/A001913
# http://mathworld.wolfram.com/DecimalExpansion.html
# http://mathworld.wolfram.com/MultiplicativeOrder.html
# http://eli.thegreenplace.net/2009/02/25/project-euler-problem-26


def multOrder(n, k=10):
  m = 1
  while ((k**m) % n) != 1:
    m += 1
  return m

def period(n):
  while not n%2: 
    n /= 2
  while not n%5: 
    n /= 5
  if n == 1: 
    return 0
  else: 
    return multOrder(n)

arr = [(n, period(n)) for n in range(1, 1000)]
max = (0,0)
for tup in arr:
  if tup[1] > max[1]:
    max = tup

print max[0],"has period",max[1]
