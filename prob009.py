# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2

# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from sys import exit

perimeter = 1000

#  Brute force
# for a in range(1,perimeter+1):
#   for b in range (1,perimeter-a+1):

# Smarter, considering that a < b < c and a < perimeter/3 and a < b < perimeter/2

for a in range(1,(perimeter/3)+1):
  for b in range(a, (perimeter/2)+1):
    c = perimeter - a - b
    if (a**2 + b**2 == c**2):
      print "%d %d %d" % (a, b, c)
      print "product: %d" % (a*b*c)
      exit(0)
