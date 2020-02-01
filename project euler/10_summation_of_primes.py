primes = [2]

def is_prime(num, primes):
  for prime in primes:
    if num % prime == 0:
      return False
  return True

sieve = []

max = 2000000

for number in range(1, max + 1):
  sieve.append(number)

sieve[0] = 0

for i in range(3, max, 2):
  sieve[i] = 0

for i in range(2, max):
  if sieve[i] != 0:
    number = sieve[i]
    for j in range(i + sieve[i], max, sieve[i]):
        sieve[j] = 0

    

sum = 0

for prime in sieve:
  sum += prime

print(sum)
