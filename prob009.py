# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2

# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from sys import exit

total = 1000

for a in range(1,total+1):
  for b in range (1,total+1-a):
    for c in range (1,total+1-a-b):
#      print "%d %d %d" % (a, b, c)
      if (a + b + c == total):
        if (a**2 + b**2 == c**2):
          print "%d %d %d" % (a, b, c)
          print "product: %d" % (a*b*c)
          exit(0)
