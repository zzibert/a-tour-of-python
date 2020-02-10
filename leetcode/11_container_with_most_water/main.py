def maxArea(height):
    maxArea = 0
    for i in range(0, len(height)):
      for j in range(i + 1, len(height)):
        area = min(height[i], height[j]) * (j - i)
        if area > maxArea:
          maxArea = area
    return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))