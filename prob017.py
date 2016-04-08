# coding=utf-8
# Number letter counts
# Problem 17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def num2len(num):
  numbers = { 1: 3, 
              2: 3,
              3: 5,
              4: 4,
              5: 4,
              6: 3,
              7: 5,
              8: 5,
              9: 4,
             10: 3,
             11: 6,
             12: 6,
             13: 8,
             14: 8,
             15: 7,
             16: 7,
             17: 9,
             18: 8,
             19: 8,
             20: 6,
             30: 6,
             40: 5,
             50: 5,
             60: 5,
             70: 7,
             80: 6,
             90: 6,
      "hundred": 7,  # these probably aren't strictly necessary,
          "and": 3,  #    but they might be useful for future expansion
     "thousand": 8,
            }

  #print "in num2len with num=",num

  #print "6:",numbers[6]
  #print "40:",numbers[40]
  #print "hundred:",numbers['hundred']

  if num > 1000 or num < 1:
    print "Sorry.  Currently we only support 1-1000."
    return

  if num == 1000:
    return numbers[1] + numbers['thousand']

  num_letters = 0

  if len(str(num)) == 3:
    digit = str(num)[0]
    #print "hundreds digit:",digit,
    num_letters += numbers[int(digit)]
    #print "length",numbers[int(digit)],
    num_letters += numbers['hundred']
    num -= int(digit) * 100
    if num > 0:
      num_letters += numbers['and']
    #print "num_letters:",num_letters

  if len(str(num)) == 2:
    digit = str(num)[0]
    if digit == '1':
      #print "teens:",num,
      num_letters += numbers[num]
      #print "length", numbers[num],
      num = 0
    else:
      #print "tens digit:",digit,
      num_letters += numbers[int(digit)*10]
      #print "length",numbers[int(digit)*10],
      num -= int(digit) * 10
    #print "num_letters:",num_letters

  if num > 0:
    digit = str(num)
    #print "ones digit:",digit,
    num_letters += numbers[int(digit)]
    #print "length",numbers[int(digit)],
    #print "num_letters:",num_letters

  return num_letters

# print num2len(0)
# print num2len(-2)
# print num2len(1001)
# print num2len(1000)
# print num2len(987)
# print num2len(830)
# print num2len(700)
# print num2len(605)
# print num2len(68)
# print num2len(50)
# print num2len(20)
# print num2len(817)
# print num2len(16)
# print num2len(10)
# print num2len(9)
# print num2len(1)

start = 1
stop = 1000
total_letters = 0

for num in range(start,stop+1):
  total_letters += num2len(num)

print "The total number of letters used from",start,"to",stop,"is",total_letters,"."






