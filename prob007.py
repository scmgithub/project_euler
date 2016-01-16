# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?

goal = 10001
primelist = []
count = 0
candidate = 2

while count < goal:
  print "candidate: ",candidate,
  for div in primelist:
    if candidate % div == 0:
      print ""
      break
  else:
    print "prime"
    primelist.append(candidate)
    count+=1
  candidate+=1

print "prime number %d is %d." % (goal, primelist[-1])