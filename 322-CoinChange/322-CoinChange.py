# Last updated: 23/6/2025, 3:13:47 am
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
                elif dp[target] == inf: continue
                dp[target + coin] = cmin(dp[target] + 1, dp[target + coin])
        
        return -1 if dp[amount] == inf else dp[amount]