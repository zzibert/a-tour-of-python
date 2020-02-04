def removeElement(nums: [int], val: int) -> int:
  length = len(nums)
  i = 0
  while length > 0:
    if val != nums[i]:
      i += 1
    else:
      del nums[i]
    length -= 1
  return len(nums)


print(removeElement([3,2,2,3], 3))