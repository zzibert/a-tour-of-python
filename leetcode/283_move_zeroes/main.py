def moveZeroes(nums):
  length = len(nums)
  i = 0
  while i < length:
    if nums[i] == 0:
      nums.pop(i)
      nums.append(0)
      length -= 1
    else:
      i += 1
  return nums