def containsNearbyDuplicate(nums, k):
  max_index = len(nums)
  for i in range(len(nums)):
    number = nums[i]
    for j in range(i+1, i+(k+1)):
      if j < max_index:
        if number == nums[j]:
          return True
  return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3))
print(containsNearbyDuplicate([1, 0, 1, 1], 1))
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
print(containsNearbyDuplicate([99, 99], 2))