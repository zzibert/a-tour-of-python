chains = [0, 1, 2, 8]

# 1 -> 1 | 2

# 2 -> 1 | 2

# 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 | 8

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 | 10

# 4 -> 2 -> 1 | 3

def calc_chain(number, chains):
  counter = number
  sum = 0
  while number != 1:
    if number % 2 == 0:
      number = number // 2
    else:
      number = number * 3 + 1
    sum += 1
    if number < counter:
      return sum + chains[number] 

max = 0
starting_number = 0
for i in range(4, 1000000):
  length = calc_chain(i, chains)
  if length > max:
    max = length
    starting_number = i
  chains.append(length)

print(starting_number)

# 


    
