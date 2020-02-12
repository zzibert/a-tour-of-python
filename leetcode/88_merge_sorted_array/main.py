
def merge(nums1, m, nums2, n):
  
  for i in range(n):
    nums1.pop()
  length = len(nums1)
  i = 0
  for number in nums2:
    while True:
      if length == 0:
        nums1.append(number)
        length += 1
        break
      if number <= nums1[i]:
        nums1.insert(i, number)
        length += 1
        break
      if i == (length-1):
        nums1.append(number)
        length += 1
        break
      i += 1
  return nums1

print(merge([1,2,3,0,0,0], 3, [2, 5, 6], 3))
print(merge([0], 0, [1], 1))
print(merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
print(merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5))