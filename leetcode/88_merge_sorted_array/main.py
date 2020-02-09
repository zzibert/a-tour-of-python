def merge(nums1, m, nums2, n):
  index = 0
  nums1 = nums1[0:(len(nums1) - n)]
  for i in range(0, len(nums2)):
    while index < len(nums1):
      if nums2[i] <= nums1[index]:
        nums1.insert(index, nums2[i])
        break
      else:
        index += 1
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    