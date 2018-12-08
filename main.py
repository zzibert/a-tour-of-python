prime_dict = {
    2: 0,
    3: 0,
    5: 0,
    7: 0,
    11: 0,
    13: 0,
    17: 0,
    19: 0
}

primes = [2, 3, 5, 7, 11, 13, 17, 19]

for num in range(2, 21):
    for prime in primes:
        counter = 0
        while True:
            if num % prime == 0:
                counter += 1
                num /= prime
            else:
                break
        if counter > prime_dict[prime]:
            prime_dict[prime] = counter

suma = 1
for key, value in prime_dict.items():
    if( value != 0):
        suma *= (key ** value)

print(suma)
    