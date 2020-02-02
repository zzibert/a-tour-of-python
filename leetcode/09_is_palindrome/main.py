def isPalindrome(x: int) -> bool:
  array = [s for s in str(x)]
  length = len(array)
  for i in range(0, length // 2):
    if array[i] != array[(length - 1) -i]:
      return False
  return True