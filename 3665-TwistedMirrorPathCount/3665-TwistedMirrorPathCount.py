# Last updated: 10/31/2026, 2:44:09 PM
1class Solution:
2    def uniquePaths(self, grid: List[List[int]]) -> int:
3        mod = 10**9 + 7
4        m = len(grid)
5        n = len(grid[0])
6
7        DIR = [(1, 0), (0, 1)]
8
9        @cache
10        def rec(i, j, prev_dir):
11            if i == m-1 and j == n-1: return 1
12            if grid[i][j] == 1:
13                new_dir = (prev_dir + 1) % 2
14                i2 = DIR[new_dir][0] + i
15                j2 = DIR[new_dir][1] + j
16                return rec(i2, j2, new_dir) if 0 <= i2 < m and 0 <= j2 < n else 0
17
18            ans = 0
19            for d, (i2, j2) in enumerate(DIR):
20                i2 += i
21                j2 += j
22
23                if 0 <= i2 < m and 0 <= j2 < n:
24                    ans += rec(i2, j2, d)
25            return ans % mod
26
27        ans = rec(0, 0, 0)
28        rec.cache_clear()
29        return ans