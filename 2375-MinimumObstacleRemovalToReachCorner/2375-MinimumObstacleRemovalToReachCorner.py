# Last updated: 12/6/2025, 5:38:18 am
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        stack = deque([(0 + (grid[0][0] == 1), 0, 0)])
        DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        grid[0][0] = -1

        while stack:
            obs, i, j = stack.popleft()

            if i == m-1 and j == n-1: return obs

            for x, y in DIR:
                i2 = i+x
                j2 = j+y
                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] != -1:
                    new_obs = obs + (grid[i2][j2] == 1)

                    if grid[i2][j2]:
                        stack.append((new_obs, i2, j2))
                    else:
                        stack.appendleft((new_obs, i2, j2))

                    grid[i2][j2] = -1
        return m*n