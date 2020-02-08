def plusOne(digits):
    digits[-1] += 1
    for i in range(len(digits) - 1, 0, -1):
      if digits[i] == 10:
        digits[i] = 0
        digits[i-1] += 1
      else:
        return digits
    if digits[0] == 10:
      digits[0] = 0
      digits.insert(0, 1)
    return digits


print(plusOne([1, 2, 3, 4, 5]))
print(plusOne([1, 2, 3, 4, 9]))
print(plusOne([9, 9, 9, 9, 9]))
