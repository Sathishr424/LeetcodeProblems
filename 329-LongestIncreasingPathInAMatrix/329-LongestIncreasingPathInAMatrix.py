# Last updated: 12/6/2025, 5:50:29 am
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        memo = [[-1] * n for _ in range(m)]

        def check(i, j, prev):
            if 0 <= i < m and 0 <= j < n and matrix[i][j] > prev: return dfs(i, j) + 1
            return 0

        def dfs(i, j):
            if memo[i][j] != -1: return memo[i][j]
            ans = 1

            ans = max(ans, check(i+1, j, matrix[i][j]))
            ans = max(ans, check(i, j+1, matrix[i][j]))
            ans = max(ans, check(i-1, j, matrix[i][j]))
            ans = max(ans, check(i, j-1, matrix[i][j]))

            memo[i][j] = ans
            return ans

        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        
        return res