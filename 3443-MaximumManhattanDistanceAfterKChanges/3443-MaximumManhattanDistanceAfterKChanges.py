# Last updated: 20/6/2025, 8:25:03 am
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        inf = 200
        dis = [[inf] * n for _ in range(n)]
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = deque([])

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i, j, 0))
        
        while stack:
            i, j, d = stack.popleft()
            if dis[i][j] <= d: continue
            dis[i][j] = d

            for i2, j2 in DIR:
                i2 += i
                j2 += j
                if 0 <= i2 < n and 0 <= j2 < n and grid[i2][j2] == 0:
                    stack.append((i2, j2, d+1))

        ret = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    ret = max(ret, dis[i][j])
        
        return -1 if ret == inf else ret