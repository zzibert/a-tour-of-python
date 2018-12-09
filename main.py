
dictionary = dict()

limit = 2000000

for i in range(2, limit):
    dictionary[i] = 1

for i in range(2, limit):
    counter = 2 * i
    while counter < limit:
        dictionary[counter] = 0
        counter += i

suma = 0
for i in range(2, limit):
    if dictionary[i] == 1:
        suma += i

print(suma)







