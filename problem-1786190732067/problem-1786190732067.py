# Last updated: 8/8/2026, 5:35:32 PM
1class Solution:
2    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
3        m = len(grid)
4        n = len(grid[0])
5
6        @cache
7        def rec(col, prev_col):
8            if col == n: return 0
9            ans = rec(col + 1, prev_col) + 1
10            if prev_col == -1:
11                return min(rec(col + 1, col), ans)
12            for i in range(m):
13                if abs(grid[i][col] - grid[i][prev_col]) > limit:
14                    return ans
15            
16            return min(ans, rec(col + 1, col))
17        
18        ans = rec(0, -1)
19        rec.cache_clear()
20        return n - ans