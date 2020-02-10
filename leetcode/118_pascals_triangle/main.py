def generate(numRows):
  array = []
  superArray =[]
  for i in range(1, numRows+1):
    if i == 1:
      array = [1]
    if i == 2:
      array = [1, 1]
    else:
      newArray = []
      for j in range(i):
        if j == 0 or j == (i-1):
          newArray.append(1)
        else:
          newArray.append(array[j] + array[j-1])
      array = newArray
    superArray.append(array)
  return superArray

print(generate(6))

