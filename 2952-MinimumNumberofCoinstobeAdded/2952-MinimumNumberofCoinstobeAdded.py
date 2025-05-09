# Last updated: 9/5/2025, 6:38:53 pm
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for tot in range(coin, amount+1):
                dp[tot] += dp[tot-coin]

        return dp[amount]