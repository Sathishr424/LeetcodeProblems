# Last updated: 12/6/2025, 5:37:35 am
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        q = []
        for i in range(len(queries)):
            q.append((queries[i], i))

        q_len = len(q)
        q.sort()
        
        ret = [0] * len(q)
        DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        visited = [[0] * n for _ in range(m)]
        visited[0][0] = 1

        q_index = 0
        curr_val = 0

        stack = [(grid[0][0], 0, 0)]

        while stack:
            grid_val, i, j = heapq.heappop(stack)

            if grid_val >= q[q_index][0]:
                while q_index < q_len and grid_val >= q[q_index][0]:
                    ret[q[q_index][1]] = curr_val
                    q_index += 1
                
                if q_index == q_len: break
            
            curr_val += 1
            for y, x in DIR:
                new_y = i + y
                new_x = j + x

                if 0 <= new_x < n and 0 <= new_y < m and visited[new_y][new_x] == 0:
                    visited[new_y][new_x] = 1
                    heapq.heappush(stack, (grid[new_y][new_x], new_y, new_x))
        
        while q_index < q_len:
            ret[q[q_index][1]] = curr_val
            q_index += 1
        
        return ret


