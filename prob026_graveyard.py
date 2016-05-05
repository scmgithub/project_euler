# coding=utf-8
# Reciprocal cycles
# Problem 26

#  This is a dumping ground for code related to Problem 26.

#  Below is a bunch of code I wrote (or adapted from online sources) while investigating this problem,
#    with varied levels of success.
#    No guarantee any of it works.

def isRegularNumber(n):
  if n == 1:
    return True
  while n>1 and (n%5 == 0 or n%2 == 0):
    if n%5 == 0:
      n /= 5
    if n%2 == 0:
      n /= 2

  if n == 1:
    return True
  else:
    return False

top = 1000
longest_cycle_length = 0
longest_cycle_num = 0
for d in range (1,top):
  if isRegularNumber(d):
    print d,"is a regular number"
    continue

  k = 0
  s = 0
  t = 1
  powers = {}
  powerOfTen = 1

  while not(powers.has_key(t)):
    powers[t] = k
    t = (t*10)%d
    k += 1
    print "powers:",powers
    print "t:",t
    print "k:",k
  s=powers[t]
  t = k - s
  
  print d,"has period",t,
  if t > longest_cycle_length:
    print "<-- biggest so far"
    longest_cycle_length = t
    longest_cycle_num = d
  else:
    print
  # holdit = raw_input("Enter to continue")

print "DONE:",longest_cycle_num,"has decimal period",longest_cycle_length

exit()

task = 1000
max = 0
maxval = 0
for i in range(1,task):
  if isRegularNumber(i):
    continue
  k=0
  s=0
  t=1
  powers={}
  powerOfTen = 1
  while not(powers.has_key(t)):
    powers[t] = k
    t = (t*10)%i
    k += 1
  s=powers[t]
  t = k - s
  print i,"has period",t
  if t > maxval:
    maxval = t
    max = i
print "DONE:",max,"has period", maxval


exit()

primes=[2, 3, 5, 7] 
for i in range(8, 1000): 
  a=1 
  b=int(i**0.5)+3 
  for k in primes: 
    if k>b: 
      break 
    if i%k==0: 
      a=0 
      break 
  if a==1: 
    primes.append(i) 
primes.reverse() 
for i in primes: 
  tjek=map(lambda x: 10**(x-1)-1, range(2, i)) 
  a=map(lambda x: x%i, tjek) 
  if a.count(0)==0: 
    print i 
    break

exit()

def Nines(x):
  j=0 
  for i in range(0,x):
    j += (10**i)*9
  return j
z=0
maxi = 0
for i in range(1,1000):
  if isRegularNumber(i):
    continue
  done="no" 
  x=0 
  j=i/2 
  k=i/5 
  if 2*j==i or 5*k==i:
    done="yes"
  while done=="no":
    x=x+1
    m= Nines(x)/i
    if m*i == Nines(x):
      done="yes"
  
  print i,"has period",x

  if x>z:
    maxi = i
    z=x
print "Done!",maxi,"has period",z

exit()

#
#  The code below this line definitely doesn't work.
#


def f(n, d):
    x = n * 9
    z = x
    k = 1
    while z % d:
        z = z * 10 + x
        k += 1
    return k, z / d

(len, digits) = f(1,3)
print "f(1,3): length:",len, "digits:", digits 

#(len, digits) = f(1,6)
#print "f(1,6): length:",len, "digits:", digits 

(len, digits) = f(1,7)
print "f(1,7): length:",len, "digits:", digits 

(len, digits) = f(1,9)
print "f(1,9): length:",len, "digits:", digits 

(len, digits) = f(1,11)
print "f(1,11): length:",len, "digits:", digits 

# (len, digits) = f(1,12)
# print "f(1,12): length:",len, "digits:", digits 

(len, digits) = f(1,13)
print "f(1,13): length:",len, "digits:", digits 

# (len, digits) = f(1,14)
# print "f(1,14): length:",len, "digits:", digits 

# (len, digits) = f(1,15)
# print "f(1,15): length:",len, "digits:", digits 

(len, digits) = f(1,17)
print "f(1,17): length:",len, "digits:", digits 

# (len, digits) = f(1,18)
# print "f(1,18): length:",len, "digits:", digits 

(len, digits) = f(1,19)
print "f(1,19): length:",len, "digits:", digits 

max = 0
maxn = 0
for x in range(1,1000):
  print "trying",x
  (len, digits) = f(1,x)
  if len > max:
    max = len
    maxn = x

print maxn,"has length",max

exit()

precision = 3000
from decimal import *
getcontext().prec = precision
import re

longest_cycle_length = 0

pattern_detector = re.compile(ur'(.+?)\1+')

# test_str = "0.001002004008016032064128256513026052104208416833667"
# pattern = re.findall(pattern_detector, test_str)

# print len(pattern[0]),":",pattern[0]
# exit()

for d in range(2,1000):
  getcontext().clear_flags()
  # frac_s = format(Decimal(1)/Decimal(d),"."+str(precision)+"f")
  # print "1/%d = %s" %(d,frac_s)

  frac_d = Decimal.normalize(Decimal(1)/Decimal(d))
  frac_s = str(frac_d)
  print "1/%d = %s" %(d,frac_s)
  # if getcontext().flags[Rounded]:
  #   print "Rounded",
  #   frac_s = frac_s[:-1]
  #   print "1/%d = %s" %(d,frac_s)

  if len(frac_s) < precision+1:
    print "no cycle"
    continue

  print "cycle possible"
  pattern = re.findall(pattern_detector,frac_s)
  print len(pattern[0]),":",pattern[0]
  if len(pattern[0]) > longest_cycle_length:
    print "longest so far"
    longest_cycle_length = len(pattern[0])

print "Longest cycle length is %d." % (longest_cycle_length)