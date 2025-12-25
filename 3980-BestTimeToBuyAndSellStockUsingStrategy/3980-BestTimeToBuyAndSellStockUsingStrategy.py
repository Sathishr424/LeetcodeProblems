# Last updated: 12/25/2025, 7:09:40 PM
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + prices[i])
            
        half_k = k // 2

        def sell(index):
            return prefix[index + half_k] - prefix[index]

        @cache
        def rec(index, used):
            if index >= n: return 0

            ans = rec(index + 1, used) + strategy[index] * prices[index]

            if not used and index + k <= n:
                ans = max(ans, rec(index + k, True) + sell(index+half_k))

            return ans

        ans = rec(0, False)
        rec.cache_clear()
        return ans