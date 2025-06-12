# Last updated: 12/6/2025, 5:46:13 am
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        island_id = 2
        island_size = {}
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        size = 0
        ret = 1

        def dfs(i, j):
            nonlocal size
            size += 1
            grid[i][j] = island_id

            for x, y in dirs:
                i2 = x+i
                j2 = y+j

                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 1:
                    dfs(i2, j2)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    island_size[island_id] = size
                    ret = max(ret, size)
                    island_id += 1
                    size = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    connection = {}
                    ans = 1
                    for x, y in dirs:
                        i2 = x+i
                        j2 = y+j
                        if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] != 0:
                            island = grid[i2][j2]
                            if island not in connection:
                                ans += island_size[island]
                                connection[island] = 1
                    ret = max(ret, ans)

        return ret