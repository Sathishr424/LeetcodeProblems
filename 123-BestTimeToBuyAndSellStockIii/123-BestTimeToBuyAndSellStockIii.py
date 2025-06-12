# Last updated: 12/6/2025, 5:52:44 am
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        profit = 0
        hold2 = -prices[0]
        profit2 = 0

        for i in range(1, len(prices)):
            hold = max(hold, -prices[i])
            profit = max(profit, hold+prices[i])
            hold2 = max(hold2, profit-prices[i])
            profit2 = max(profit2, hold2+prices[i])
        
        return profit2