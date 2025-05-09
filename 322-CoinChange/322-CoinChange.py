# Last updated: 9/5/2025, 2:28:16 pm
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(amount):
            for coin in coins:
                if coin+i <= amount:
                    dp[coin+i] = min(dp[coin+i], dp[i] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1