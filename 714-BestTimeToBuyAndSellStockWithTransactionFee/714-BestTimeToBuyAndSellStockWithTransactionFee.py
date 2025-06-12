# Last updated: 12/6/2025, 5:47:29 am
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache
        def rec(index, hold):
            if index >= len(prices): return 0
            if hold:
                ans = max(rec(index+1, hold), prices[index] + rec(index+1, not hold) - fee)
            else:
                ans = max(rec(index+1, hold), -prices[index] + rec(index+1, not hold))

            return ans
        
        return rec(0, False)
        