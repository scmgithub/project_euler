# Non-abundant sums
# Problem 23

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

print "Finding abundant numbers..."
limit = 28123
abundants = []
perfects = []
deficients = []

for x in range(1,limit+1):
  # print "trying",x,
  sum_divisors = 0 
  for n in range(1,(x/2)+1):
    if x%n == 0:
      sum_divisors += n
  # print "sum is",sum_divisors,
  if sum_divisors < x:
    # print "deficient"
    deficients.append(x)
  elif sum_divisors > x:
    # print "abundant - adding"
    abundants.append(x)
  else:
    # print "PERFECT"
    perfects.append(x)

# print "abundants:"
# print abundants

# print "PERFECTS:"
# print perfects

# print "deficients:"
# print deficients

dont_add_sum = 0
no_sums = []

for candidate in range(1,limit+1):
  dumflag = 0
  for add1 in abundants:
    if add1 > candidate:
      continue # abundants is sorted
    for add2 in abundants:
      if add2 > candidate:
        continue
      if add1 + add2 == candidate:
        print candidate,"is the sum of %d and %d - skipping" % (add1, add2)
        dumflag=1
        break
    if dumflag ==1:
      break    
  else:
    print candidate,"is not any sum - adding to result"
    dont_add_sum += candidate
    no_sums.append(candidate)

print "The sum of positive integers that cannot be written as the sum of two abundant numbers is %d." % (dont_add_sum)



