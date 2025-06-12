# Last updated: 12/6/2025, 5:36:34 am
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        theives = deque([])
        dist = [[-1] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    theives.append((i, j))
        
        while theives:
            i, j = theives.popleft()

            for y, x in DIR:
                i2 = i+y
                j2 = j+x

                if 0 <= i2 < n and 0 <= j2 < n and dist[i2][j2] == -1:
                    dist[i2][j2] = dist[i][j] + 1
                    theives.append((i2, j2))
        
        stack = [(-dist[0][0], 0, 0)]

        while stack:
            safe, i, j = heapq.heappop(stack)
            safe = -safe

            if i == n-1 and j == n-1:
                return safe

            for y, x in DIR:
                i2 = i+y
                j2 = j+x

                if 0 <= i2 < n and 0 <= j2 < n and grid[i2][j2] == 0:
                    grid[i2][j2] = -1
                    heapq.heappush(stack, (-min(safe, dist[i2][j2]), i2, j2))

        return 0