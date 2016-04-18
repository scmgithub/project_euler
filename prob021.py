# coding=utf-8
# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

max = 10000
amicable_sum = 0
d = []
d.append(0)  # d(0) = 0
d.append(0)  # d(1) = 0

for n in range(2,max):
  # print "n:",n
  d.append(1)  # everybody > 1 is divisible by 1
  for x in range(2,(n/2)+1):
    # print "x:",x,
    if n%x == 0:
      d[n] += x
  # print

for i in range(0,len(d)):
  # print "%d: %d" % (i, d[i])
  if d[i] > 0 and d[i] < max and i != d[i] and i == d[d[i]]:
    # print "AMICABLE\t%d: %d" % (d[i], d[d[i]])
    amicable_sum += d[i]
    amicable_sum += d[d[i]]
      # Note, we will count each amicable number twice.  So divide by two below.

amicable_sum /= 2

print "The sum of all amicable numbers under %d is %d." % (max, amicable_sum)
