# Last updated: 10/28/2026, 12:35:43 PM
1class Solution:
2    def minCost(self, grid: list[list[int]]) -> int:
3        m = len(grid)
4        n = len(grid[0])
5        inf = 10**9
6
7        DIR = [(1, 0), (0, 1)]
8        max_value = max([max(grid[i]) for i in range(m)])
9        set_bits = max_value.bit_length()
10        max_value = 1 << set_bits
11        dp = [[[-1] * max_value for _ in range(n)] for _ in range(m)]
12        def rec(i, j, curr):
13            if dp[i][j][curr] != -1: return dp[i][j][curr]
14            if i == m-1 and j == n-1: return curr
15            
16            ans = inf
17            for i2, j2 in DIR:
18                i2 += i
19                j2 += j
20                if 0 <= i2 < m and 0 <= j2 < n:
21                    ans = min(rec(i2, j2, curr ^ grid[i2][j2]), ans)
22
23            dp[i][j][curr] = ans
24            return ans
25        
26        ans = rec(0, 0, grid[0][0])
27        return ans