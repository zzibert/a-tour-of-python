chains = [0, 1]
m = 0
result = 0

for start in range(2, 1000000):
    num = start
    index = 1
    length = 0
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = 3 * num + 1
        length += 1
        if num < start:
            length += chains[num]
            break
    chains.append(length)

for index in range(len(chains)):
    if m < chains[index]:
        m = chains[index]
        result = index

    
print(result)









