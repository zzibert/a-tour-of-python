def majorityElement(nums):
  n = len(nums) / 2
  values = {}
  for element in nums:
    if not element in values:
      values[element] = 1
    else:
      values[element] += 1
      if values[element] >= n:
        return element

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))