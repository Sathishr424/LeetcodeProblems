# Last updated: 12/6/2025, 5:51:54 am
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parents = [i for i in range(m*n)]
        sizes = [1] * (m*n)
        dirs = [(0, 1), (1, 0)]
        ret = {}

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            nonlocal ret
            node1 = find(x)
            node2 = find(y)
            # print(x, y, node1, node2)
            if node1 == node2: return True

            if sizes[node2] > sizes[node1]:
                node2, node1 = node1, node2
            
            sizes[node1] += sizes[node2]
            parents[node2] = node1
            return False
        island_exist = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island_exist = True
                    pos = i*n + j
                    if find(pos) == pos: 
                        ret[pos] = 1
                    for x, y in dirs:
                        ni = i+x
                        nj = j+y
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                            union(pos, ni*n + nj)
        new_ret = {}
        for pos in ret:
            new_ret[find(pos)] = 1
        ret = len(new_ret)
        return ret if ret > 0 else 1 if island_exist else 0