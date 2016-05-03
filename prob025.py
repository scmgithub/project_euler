# coding=utf-8
# 1000-digit Fibonacci number
# Problem 25

# The Fibonacci sequence is defined by the recurrence relation:

#     F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.

# Hence the first 12 terms will be:

#     F(1) = 1
#     F(2) = 1
#     F(3) = 2
#     F(4) = 3
#     F(5) = 5
#     F(6) = 8
#     F(7) = 13
#     F(8) = 21
#     F(9) = 34
#     F(10) = 55
#     F(11) = 89
#     F(12) = 144

# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

digits = 1000
a = 1
b = 1
c = a + b
index = 3

while len(str(c)) < digits:
    a = b
    b = c
    c = a + b
    index += 1
    # print c,"is",len(str(c)),"digits long"

print "Fib(%d) = %d is %d digits long." % (index, c, digits)

