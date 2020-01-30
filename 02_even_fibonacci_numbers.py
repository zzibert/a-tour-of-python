num1 = 1
num2 = 1

counter = 4000000
i = 0
sum = 0

while num2 < counter:
  temp = num1
  num1 = num2
  num2 = temp + num1
  if num2 % 2 == 0:
    sum += num2
  i += 1

print(sum)