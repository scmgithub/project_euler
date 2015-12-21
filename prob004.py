# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


#  This could be done more efficiently.  -scm


def ispalindrome(thing):
  thing = str(thing)
  if thing == thing[::-1]:
    return True
  else:
    return False

max = 999
bigpal = 0

for i in range(max,max / 10,-1):
  for j in range(max,max / 10,-1):
    product=i*j
    if ispalindrome(product) and product > bigpal:
      bigpal = product

print "The largest palindrome made from the product of two numbers <= %d is %d." % (max, bigpal)
