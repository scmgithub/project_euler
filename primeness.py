import math

primes = [2,3]

def extend_primes(upto):
    """Pre-extend the table of known primes"""
    for candidate in range(primes[-1]+2, upto + 1, 2):
        if is_prime(candidate):
            primes.append(candidate)

def is_prime(x):
    """Check whether "x" is a prime number"""
    # Check for too small numbers
    if x < primes[0]:
        return False
    # Calculate the largest possible divisor
    max = int(math.sqrt(x))
    # First, check against known primes
    for prime in primes:
        if prime > max:
            return True
        if x % prime == 0:
            return False
    # Then, lazily extend the table of primes as far as necessary
    for candidate in range(prime[-1], max + 1, 2):
        if is_prime(candidate):
            primes.append(candidate)
            if x % candidate == 0:
                return False
    return True

def isprime(n):
  if n<=1:
    return False
  if n<4:
    return True
  if n % 2 == 0:
    return False
  if n < 9:
    return True
  if n % 3 == 0:
    return False

  div = 5
  while div <= int(math.sqrt(n)):
    if n % div == 0:
      return False
    if n % (div+2) == 0:
      return False
    div += 6
  return True

def primefactor(n):
  if n > primeness.primes[-1]:
    primeness.extend_primes(n)

  stop = n
  factors = []
  for prime in primeness.primes:
    if prime > stop:
      break
    while n%prime == 0:
      factors.append(prime)
      n /= prime
  return factors