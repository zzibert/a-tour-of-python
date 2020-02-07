def maxProfit(prices):
  if len(prices) == 0:
    return 0
  
  buy = prices[0]
  sell = max(prices[1:])
  profit = sell - buy
  for i in range(1, len(prices)):
    if prices[i] < buy:
      if (max(prices[i:]) - prices[i]) > profit:
        buy = prices[i]
        profit = (max(prices[i:]) - prices[i])
  return profit, sell

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([1, 2]))