def is_palindrome(number):
    arr1 = list(str(number))
    arr2 = list(reversed(arr1))
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

biggest = 0

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        result = num1 * num2
        if is_palindrome(result):
            if biggest < result:
                biggest = result

print(biggest)