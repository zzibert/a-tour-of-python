def searchInsert(nums , target ):
  for i in range(0, len(nums)):
    if nums[i] == target:
      return i
    elif nums[i] > target:
      return i
  return len(nums)
