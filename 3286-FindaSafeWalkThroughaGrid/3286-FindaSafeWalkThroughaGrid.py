# Last updated: 7/2/2026, 2:58:08 PM
1from typing import List
2DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
3
4class Solution:
5    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
6        m = len(grid)
7        n = len(grid[0])
8        vis = [[-1] * n for _ in range(m)]
9
10        def dfs(i, j, rem):
11            if rem <= 0: return False
12            if i == m-1 and j == n-1: return True
13            for i2, j2 in DIR:
14                i2 += i
15                j2 += j
16
17                if 0 <= i2 < m and 0 <= j2 < n:
18                    new_rem = rem - grid[i2][j2]
19                    if new_rem > vis[i2][j2]:
20                        vis[i2][j2] = new_rem
21                        if dfs(i2, j2, new_rem): return True
22            return False
23
24        vis[0][0] = health - grid[0][0]
25        return dfs(0, 0, health - grid[0][0])