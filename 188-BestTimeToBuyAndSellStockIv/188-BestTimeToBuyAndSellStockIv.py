# Last updated: 12/6/2025, 5:52:02 am
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        inf = float('inf')
        n = len(prices)
        @cache
        def rec(index, state, rem):
            if rem == 0 and state == 0: return 0
            if rem < 0: return -inf
            if index >= n: return 0 if state == 0 else -inf

            ans = rec(index+1, state, rem)

            if state == 0:
                ans = max(ans, rec(index+1, 1, rem-1) - prices[index])
            else:
                ans = max(ans, rec(index+1, 0, rem) + prices[index])
            
            return ans
        
        ans = rec(0, 0, k)
        rec.cache_clear()
        return ans