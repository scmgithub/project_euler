# Problem 2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a = 1
b = 2
eventotal = 2
sum = 2
limit = 4000000

while a+b <= limit:
  sum = a + b
  if sum % 2 == 0:
    eventotal += sum
  a = b
  b = sum

print "The sum of the even-valued terms of the Fibonacci sequence whose values do not exceed %d is %d." % (limit, eventotal)
