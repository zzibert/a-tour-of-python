num1 = 100
num2 = 100

def is_palindrome(list):
  for counter in range(0, len(list) // 2):
    if list[counter] != list[len(list) - (counter +1)]:
      return False
  return True

max = 0

for num1 in range(100, 1000):
  for num2 in range(100, 1000):
    palindrome = num1 * num2
    list = [int(i) for i in str(palindrome)]
    if is_palindrome(list) and max < palindrome:
      max = palindrome

print(max)




