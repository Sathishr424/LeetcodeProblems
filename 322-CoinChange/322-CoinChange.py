# Last updated: 23/6/2025, 3:04:08 am
inf = float('inf')
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        @cache
        def rec(target):
            if target == 0:
                return 0
            
            ans = inf
            for coin in coins:
                if target-coin < 0: break
                ans = min(ans, rec(target - coin) + 1)
            return ans
        
        ans = rec(amount)
        return -1 if ans == float('inf') else ans