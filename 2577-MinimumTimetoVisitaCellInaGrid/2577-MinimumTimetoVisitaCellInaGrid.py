# Last updated: 7/5/2025, 7:25:17 pm
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        
        stack = [(0, 0, 0)]

        while stack:
            time, i, j = heapq.heappop(stack)
            if i == m-1 and j == n-1: return time
            
            new_time = time+1

            for ni, nj in DIR:
                ni += i
                nj += j

                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == -1: continue

                    heapq.heappush(stack, (max(new_time, grid[ni][nj] + ((grid[ni][nj] - new_time) % 2)), ni, nj))
                    
                    grid[ni][nj] = -1
            
        return -1