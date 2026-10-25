# Last updated: 10/25/2026, 1:56:49 PM
1class Solution:
2    def closedIsland(self, grid: list[list[int]]) -> int:
3        m = len(grid)
4        n = len(grid[0])
5
6        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
7
8        def dfs(i, j):
9            grid[i][j] = 1
10            for i2, j2 in DIR:
11                i2 += i
12                j2 += j
13
14                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 0:
15                    dfs(i2, j2)
16
17        for i in range(m):
18            for j in [0, n-1]:
19                if grid[i][j] == 0:
20                    dfs(i, j)
21
22        for j in range(1, n-1):
23            for i in [0, m-1]:
24                if grid[i][j] == 0:
25                    dfs(i, j)
26
27        ans = 0
28        for i in range(1, m-1):
29            for j in range(1, n-1):
30                if grid[i][j] == 0:
31                    dfs(i, j)
32                    ans += 1
33
34        return ans