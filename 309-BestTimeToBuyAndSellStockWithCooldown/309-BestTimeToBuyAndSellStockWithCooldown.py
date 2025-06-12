# Last updated: 12/6/2025, 5:50:41 am
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def rec(index, hold):
            if index >= len(prices): return 0
            if hold:
                ans = max(rec(index+1, hold), prices[index] + rec(index+2, not hold))
            else:
                ans = max(rec(index+1, hold), -prices[index] + rec(index+1, not hold))

            return ans
        
        return rec(0, False)
        