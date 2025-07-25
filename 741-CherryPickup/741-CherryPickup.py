# Last updated: 26/7/2025, 5:01:11 am
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid)

        @cache
        def canReachIt(i, j):
            if i == n-1 and j == n-1: return True

            if i + 1 < n and grid[i + 1][j] != -1:
                if canReachIt(i + 1, j): return True
            elif j + 1 < n and grid[i][j + 1] != -1:
                if canReachIt(i, j + 1): return True
            return False
    
        if grid[0][0] == -1: return 0

        def visit(i, j, i2, j2):
            ans = -inf
            add = grid[i][j]
            if i2 != i and j2 != j:
                add += grid[i2][j2]
            if i + 1 < m and grid[i+1][j] != -1:
                can = False
                if i2 + 1 < m and grid[i2+1][j2] != -1:
                    ans = max(ans, dfs(i + 1, j, i2 + 1, j2) + add)
                if j2 + 1 < m and grid[i2][j2+1] != -1:
                    ans = max(ans, dfs(i + 1, j, i2, j2 + 1) + add)
                if i2 == m-1 and j2 == m-1:
                    ans = max(ans, dfs(i + 1, j, i2, j2) + add)
            
            if j + 1 < m and grid[i][j + 1] != -1:
                if i2 + 1 < m and grid[i2+1][j2] != -1:
                    ans = max(ans, dfs(i, j + 1, i2 + 1, j2) + add)
                if j2 + 1 < m and grid[i2][j2+1] != -1:
                    ans = max(ans, dfs(i, j + 1, i2, j2 + 1) + add)
                if i2 == m-1 and j2 == m-1:
                    ans = max(ans, dfs(i, j + 1, i2, j2) + add)
            return ans

        @cache
        def dfs(i, j, i2, j2):
            if i == n-1 and j == n-1 and i2 == n-1 and j2 == n-1:
                return grid[i][j]
                
            return max(visit(i, j, i2, j2), visit(i2, j2, i, j))
            
        
        return max(0, dfs(0, 0, 0, 0))