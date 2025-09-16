# Last updated: 16/9/2025, 9:47:43 pm
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        there = defaultdict(int)
        for h, w, p in prices:
            there[(h, w)] = p

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def rec(h, w):
            if dp[h][w] != -1: return dp[h][w]
            ans = there[(h, w)]

            for half_h in range(1, h // 2 + 1):
                ans = max(ans, rec(half_h, w) + rec(h - half_h, w))
            
            for half_w in range(1, w // 2 + 1):
                ans = max(ans, rec(h, half_w) + rec(h, w - half_w))
            
            dp[h][w] = ans
            return ans

        return rec(m, n)