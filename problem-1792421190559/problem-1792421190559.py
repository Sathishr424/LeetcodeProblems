# Last updated: 10/19/2026, 8:16:30 PM
1class Solution:
2    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
3        m = len(grid)
4        n = len(grid[0])
5
6        dirs = {"R": [0, 1], 'D': [1, 0], 'L': [0, -1], 'U': [-1, 0]}
7
8        def canVisit(r, c):
9            return not (r < 0 or r >= m or c < 0 or c >= n) and grid[r][c] != 'X'
10
11        def dfs(r, c):
12            cell = grid[r][c]
13            grid[r][c] = 'X'
14            nr, nc = dirs[cell]
15            nr += r
16            nc += c
17            if canVisit(nr, nc):
18                return dfs(nr, nc)
19            return [r, c]
20
21        return dfs(0, 0)