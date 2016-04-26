# Non-abundant sums
# Problem 23

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

print "Finding abundant numbers..."
limit = 28123
abundants = []

for x in range(1,limit+1):
  sum_divisors = 0 
  for n in range(1,(x/2)+1):
    if x%n == 0:
      sum_divisors += n
  if sum_divisors > x:
    abundants.append(x)

print "Determining sums of abundants..."
abundant_sums = {}
for num1 in abundants:
  for num2 in reversed(abundants):
    if num2 < num1:
      break
    abundant_sums[num1+num2] = 1

print "Finding missing candidates..."
no_add_sum = 0
for candidate in range(1,limit+1):
  if candidate not in abundant_sums: 
    no_add_sum += candidate

print "The sum of positive integers that cannot be written as the sum of two abundant numbers is %d." % (no_add_sum)
