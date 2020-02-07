def arrayPairSum(nums):
    summa = 0
    nums = sorted(nums)
    for i in range(0, len(nums) - 1, 2):
      summa += min(nums[i], nums[i+1])
    return summa

