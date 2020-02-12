def twoSum(numbers, target):
  values = {}
  indexes = {}
  for i in range(0, len(numbers)):
    desired = target - numbers[i]
    if desired == numbers[i]:
      for j in range(i+1, len(numbers)):
        if numbers[j] == desired:
          return [i+1, j+1]
    indexes[numbers[i]] = i
    if desired in values and values[desired] == numbers[i]:
      return [indexes[desired]+1, indexes[numbers[i]]+1]
    values[numbers[i]] = desired
  
  
print(twoSum([2,3,4], 6))
print(twoSum([0,0, 3,4], 0))