def maxProfit(prices):
  maxprofit = 0
  for i in range(0, len(prices)):
    profit = -(prices[i])
    stock = prices[i]
