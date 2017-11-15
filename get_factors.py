def divisors(num):
# Given an integer, return a list of its factors. If it's prime, say so.
  primes = []
  for i in range(1, num + 1):
      if integer % i == 0:
          primes.append(i)
  if len(primes) == 2:
      return str(num) + ' is prime'
  return [x for x in primes if x not in [num, 1]]
  
# More succinctly:
def divisors2(num):
  l = [a for a in range(2, num) if num % a == 0]
  if len(l) == 0:
    return str(num) + ' is prime'
  return l
