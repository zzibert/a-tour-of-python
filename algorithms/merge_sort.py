import random

nums = [i for i in range(1,17)]

random.shuffle(nums)

def merge(nums):
    length = len(nums)
    if length == 2:
      return sorted(nums)
    else:
      return sorted(merge(nums[:(length // 2)]) + merge(nums[(length // 2):]))

print(nums)
print(merge(nums))