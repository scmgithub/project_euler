# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

div1=3
div2=5
limit=1000
multsum=0

for i in range(limit):
  if i % div1 == 0 or i % div2 == 0:
    multsum+=i

print "The sum of all multiples of %d or %d below %d is %d." % (div1, div2, limit, multsum)
