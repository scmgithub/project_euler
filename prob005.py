# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

max = 20
candidate = max
found = False

# while found == False:
#   for div in range(2,max):
#     if candidate % div != 0:
#       candidate+=1
#       break
#   else:
#     print "I think we found ",candidate
#     found = True

while found == False:
  print "candidate: ", candidate,
  for div in range(2,max):
    if candidate % div != 0:
      print " fails on ",div
      candidate+=max
      break
  else:
    print "I think we found ",candidate
    found = True
