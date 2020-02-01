primes = [2]

def is_prime(num, primes):
  for prime in primes:
    if num % prime == 0:
      return False
  return True

counter = 1
number = 3

while counter < 10001:
  if is_prime(number, primes):
    primes.append(number)
    counter += 1
  number += 1

print(primes[10000])