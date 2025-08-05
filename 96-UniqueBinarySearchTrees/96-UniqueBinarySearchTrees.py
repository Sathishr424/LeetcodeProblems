# Last updated: 5/8/2025, 10:41:57 am
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def rec(i, j):
            if i == m-1 and j == n-1:
                return 1
            
            ans = 0
            if i + 1 < m:
                ans += rec(i + 1, j)
            if j + 1 < n:
                ans += rec(i, j + 1)
            return ans
        
        return rec(0, 0)