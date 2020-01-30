def is_prime(num, primes):
  for prime in primes:
    if num % prime == 0:
      return False
  return True
  