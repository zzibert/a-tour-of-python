primes = [2]

counter = 600851475143
max = 1
i = 3

def is_prime(num, primes):
  for prime in primes:
    if num % prime == 0:
      return False
  return True

def division(num, divider):
  num = num / divider
  return num

while counter != 1:
  if is_prime(i, primes):
    primes.append(i)
    while counter % i == 0:
      max = i
      print(counter)
      counter = counter / i

  i += 1

print(primes)
print(max)
