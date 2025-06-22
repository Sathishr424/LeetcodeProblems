# Last updated: 23/6/2025, 3:11:54 am
inf = float('inf')
cmin = lambda x, y: x if x < y else y
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for target in range(amount):
            for coin in coins:
                if target + coin > amount: break
                dp[target + coin] = cmin(dp[target] + 1, dp[target + coin])
                if target + coin == amount: break
        
        return -1 if dp[amount] == inf else dp[amount]