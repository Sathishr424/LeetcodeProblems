# Last updated: 10/26/2026, 11:20:32 AM
1class Solution:
2    def countIslands(self, grid: List[List[int]], k: int) -> int:
3        m = len(grid)
4        n = len(grid[0])
5
6        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
7
8        def dfs(i, j):
9            tot = grid[i][j]
10            grid[i][j] = 0
11            for i2, j2 in DIR:
12                i2 += i
13                j2 += j
14
15                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] > 0:
16                    tot += dfs(i2, j2)
17
18            return tot % k
19
20        ans = 0
21        for i in range(m):
22            for j in range(n):
23                if grid[i][j] > 0 and dfs(i, j) == 0: ans += 1
24
25        return ans