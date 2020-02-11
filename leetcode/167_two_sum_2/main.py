def twoSum(numbers, target):
  values = {}
  indexes = {}
  for i in range(0, len(numbers)):
    indexes[numbers[i]] = i
    desired = target - numbers[i]
    values[numbers[i]] = desired
    if desired in values and values[desired] == numbers[i]:
      return [indexes[desired]+1, indexes[numbers[i]]+1]
  
  
print(twoSum([2,3,4], 6))