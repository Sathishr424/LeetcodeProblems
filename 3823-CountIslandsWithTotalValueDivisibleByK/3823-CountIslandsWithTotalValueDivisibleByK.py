# Last updated: 12/25/2025, 7:11:45 PM
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        tot = m * n
        parents = [i for i in range(tot)]
        sizes = [0] * tot

        for i in range(m):
            for j in range(n):
                sizes[i * n + j] = grid[i][j]
                
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])

            return parents[x]

        def union(x, y):
            x = find(x)
            y = find(y)

            if x == y: return True
            if sizes[y] > sizes[x]:
                x, y = y, x
            sizes[x] += sizes[y]
            parents[y] = x
            return False

        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                pos = i * n + j
                for i2, j2 in DIR:
                    i2 += i
                    j2 += j
                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] > 0:
                        union(pos, i2 * n + j2)

        used = [0] * tot
        ret = 0
        for i in range(tot):
            par = find(i)
            if used[par]: continue
            used[par] = 1
            if sizes[par] > 0 and sizes[par] % k == 0:
                ret += 1

        return ret