# coding=utf-8
# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

months = {  'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31
         }
days = {  0: 'Sunday',
          1: 'Monday',
          2: 'Tuesday',
          3: 'Wednesday',
          4: 'Thursday',
          5: 'Friday',
          6: 'Saturday',
       }

dow = 1  # Monday - 19000101 was Monday
fom_sun = 0

for year in range(1900,2001):
  for month in ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'):
    # print month, "1st", year, "was a", days[dow], "(", dow, "). Add", months[month]
    dow += months[month]
    if month is 'February':
      if year%4 == 0:
        if year%100 != 0 or year%400 == 0:
          dow += 1  # leap day
          # print "add one leap day"
    dow %= 7
    if dow == 0 and year > 1900:
      fom_sun += 1

print "Sunday was the first day of the month %d times." % (fom_sun)
