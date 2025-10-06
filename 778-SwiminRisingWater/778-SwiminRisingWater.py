# Last updated: 6/10/2025, 10:05:54 am
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(grid[0][0], 0, 0)]
        dis = [[inf] * n for _ in range(m)]

        while heap:
            t, i, j = heapq.heappop(heap)
            if i == m-1 and j == n-1: return t

            if dis[i][j] <= t: continue
            dis[i][j] = t

            for i2, j2 in DIR:
                i2 += i
                j2 += j
                if 0 <= i2 < m and 0 <= j2 < n:
                    new_t = max(grid[i2][j2], t)
                    if dis[i2][j2] > new_t:
                        heapq.heappush(heap, (new_t, i2, j2))
        
        return max([max(row) for row in grid])