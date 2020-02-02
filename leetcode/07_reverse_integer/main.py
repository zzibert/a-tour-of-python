def reverse(x: int) -> int:
  if x == 0:
    return 0
  is_negative = False
  if x < 0:
    x = abs(x)
    is_negative = True
  array = [int(y) for y in str(x)]
  while array[-1] == 0:
      array.pop()
  array.reverse()
  st = ''.join(str(x) for x in array)
  if is_negative:
    number = int('-' + st)
  else:
    number = int(st)
  if -(2 ** 31 - 1) > number or (2 ** 31) < number:
    return 0
  else:
    return number