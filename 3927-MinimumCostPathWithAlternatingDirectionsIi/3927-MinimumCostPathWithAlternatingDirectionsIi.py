# Last updated: 12/25/2025, 7:10:44 PM
inf = float('inf')
class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        @cache
        def rec(i, j, s):
            if i == m-1 and j == n-1:
                return 0
            cost = 0
            if s == 0 and i * n + j > 0:
                s = 1
                cost += waitCost[i][j]
            ans = inf
            if i + 1 < m:
                ans = min(ans, rec(i + 1, j, (s + 1) % 2) + cost + (i + 2) * (j + 1))
            if j + 1 < n:
                ans = min(ans, rec(i, j + 1, (s + 1) % 2) + cost + (i + 1) * (j + 2))
            return ans
        
        ans = rec(0, 0, 1) + 1
        rec.cache_clear()
        return ans