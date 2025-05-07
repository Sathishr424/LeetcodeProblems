# Last updated: 7/5/2025, 7:19:00 pm
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
                    
                    if new_time < grid[ni][nj]:
                        diff = grid[ni][nj] - new_time
                        new_time_larger = time + diff + (2 if diff % 2 else 1)
                        
                        heapq.heappush(stack, (new_time_larger, ni, nj))
                    elif new_time >= grid[ni][nj]:
                        heapq.heappush(stack, (new_time, ni, nj))
                    
                    grid[ni][nj] = -1
            
        return -1