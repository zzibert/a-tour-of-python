


def is_divisible(num):
  for i in range(2, 21):
    if num % i != 0:
      return False
  return True

counter = 20

while True:
  if is_divisible(counter):
    print(counter)
    break
  counter += 20