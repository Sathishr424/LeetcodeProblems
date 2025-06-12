# Last updated: 12/6/2025, 5:46:57 am
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # 0,1 1,2 2,3
        # 0,2 1,3 2,4

        def dfs(i, j, val):
            if i == m or j == n: return True
            if matrix[i][j] != val: return False
            return dfs(i+1, j+1, val)

        for j in range(n):
            if not dfs(1, j+1, matrix[0][j]): return False
        
        for i in range(1, m):
            if not dfs(i+1, 1, matrix[i][0]): return False
        
        return True