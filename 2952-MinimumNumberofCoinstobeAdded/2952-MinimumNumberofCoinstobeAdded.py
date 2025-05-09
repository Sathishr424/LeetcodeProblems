# Last updated: 9/5/2025, 6:35:43 pm
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        coins.sort()
        for coin in coins:
            for i in range(amount):
                if coin+i > amount: break
                dp[coin+i] += dp[i]
        return dp[amount]