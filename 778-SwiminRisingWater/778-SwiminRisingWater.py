# Last updated: 7/5/2025, 11:49:38 am
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        stack = [(grid[0][0], 0, 0)]
        DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while stack:
            depth, i, j = heapq.heappop(stack)
            if i == n-1 and j == n-1: return depth

            for ni, nj in DIR:
                ni += i
                nj += j

                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] != -1:
                    heapq.heappush(stack, (max(depth, grid[ni][nj]), ni, nj))
                    grid[ni][nj] = -1
        
        return grid[-1][-1]

