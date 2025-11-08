# Last updated: 9/11/2025, 1:34:16 am
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        inf = 10**20
        
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        heap = []
        heap.append((0, 0, 0))
        dis = [[inf] * n for _ in range(m)]

        canMoveFromStart = False
        for i2, j2 in [(0, 1), (1, 0)]:
            canMoveFromStart = canMoveFromStart or grid[i2][j2] <= 1
        
        if not canMoveFromStart: return -1
        while heap:
            time, i, j = heapq.heappop(heap)
            # print(time, i, j)

            if i == m-1 and j == n-1: return time
            
            if dis[i][j] <= time: continue
            dis[i][j] = time
            
            time += 1
            for i2, j2 in DIR:
                i2 += i
                j2 += j

                if 0 <= i2 < m and 0 <= j2 < n:
                    can =  grid[i2][j2]
                    need = max(0, can - time)
                    need += need % 2
                    new_time = time + need
                    if new_time >= can and dis[i2][j2] > new_time:
                        heapq.heappush(heap, (new_time, i2, j2))
        
        return -1