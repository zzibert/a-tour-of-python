def removeDuplicates(nums: [int]) -> int:
  i = 0
  current = 'a'
  length = len(nums)
  while length > 0:
    if current != nums[i]:
      current = nums[i]
      i += 1
    else:
      del nums[i]
    length -= 1
  return len(nums)


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))