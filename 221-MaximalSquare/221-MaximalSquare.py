# Last updated: 12/6/2025, 5:51:31 am
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = []
        for i in range(m+1):
            tmp = []
            for j in range(n+1):
                tmp.append(0)
            dp.append(tmp)
        
        ret = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    ret = max(ret, dp[i][j])
        return ret * ret