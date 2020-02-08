def containsDuplicate(nums):
  values = {}
  for number in nums:
    if number in values:
      return True
    else:
      values[number] = 1
  return False