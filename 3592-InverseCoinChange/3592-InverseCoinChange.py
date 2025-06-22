# Last updated: 23/6/2025, 3:33:35 am
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for tot in range(amount-coin+1):
                dp[tot + coin] += dp[tot]
        
        return dp[amount]