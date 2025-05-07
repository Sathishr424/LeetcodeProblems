# Last updated: 7/5/2025, 7:17:26 pm
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        stack = [(0, 0, 0)]

        while stack:
            time, i, j = heapq.heappop(stack)
            if i == m-1 and j == n-1: return time
            
            new_time = time+1

            for ni, nj in DIR:
                ni += i
                nj += j

                if 0 <= ni < m and 0 <= nj < n:
                    if new_time < grid[ni][nj]:
                        diff = grid[ni][nj] - new_time
                        new_time_larger = time + diff + (2 if diff % 2 else 1)
                        
                        dist[ni][nj] = new_time_larger
                        heapq.heappush(stack, (new_time_larger, ni, nj))
                    elif new_time >= grid[ni][nj] and new_time < dist[ni][nj]:
                        dist[ni][nj] = new_time
                        heapq.heappush(stack, (new_time, ni, nj))
            
        return -1