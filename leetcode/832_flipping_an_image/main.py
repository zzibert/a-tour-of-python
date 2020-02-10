def flipAndInvertImage(A):
  newArray = []
  for row in A:
    array = []
    for number in row[::-1]:
      if number == 0:
        array.append(1)
      else:
        array.append(0)
    newArray.append(array)
      

  return newArray

print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))