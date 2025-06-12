# Last updated: 12/6/2025, 5:52:48 am
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        profit = 0

        for i in range(1, len(prices)):
            hold = max(hold, -prices[i])
            profit = max(profit, hold+prices[i])
        
        return profit