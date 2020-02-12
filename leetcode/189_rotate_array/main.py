def rotate(nums, k):
  length = len(nums)
  newArray = [0 for i in nums]
  for i in range(length):
    index = (i+k) % length
    newArray[index] = nums[i]
  for i in range(length):
    nums[i] = newArray[i]
  return nums


print(rotate([1,2,3,4,5,6,7], 3))