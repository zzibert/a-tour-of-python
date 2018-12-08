counter = 3

primes = [2]

def is_prime(number, primes):
    for prime in primes:
        if number % prime == 0:
            return False
    primes.append(number)
    return True

counter = 1
number = 3

while counter < 10001:
    if is_prime(number, primes):
        counter += 1
    number += 1

print(primes)

    