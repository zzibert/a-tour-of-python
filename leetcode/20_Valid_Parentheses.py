def isValid(s: str) -> bool:
 counter = {
   "(": 0,
   "[": 0,
   "{": 0 
  }
  for char in s:
    if char == "(":
      counter["("] += 1
    else if char == ")":
      cunter[")"] -= 1
    if char == "(":
      counter["["] += 1
    else if char == "]":
      counter["]"] -= 1
    if char == "{":
      counter["{"] += 1
    else if char == "}":
      counter["}"] -= 1
  values = counter.values()
  for i in range (0, 3):
    if values[i] != 0:
      return False
  return True


