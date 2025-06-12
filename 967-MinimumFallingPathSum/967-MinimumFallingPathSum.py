# Last updated: 12/6/2025, 5:45:10 am
class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        dp = [0 for _ in range(n+1)]
        dp[0] = float('inf')
        dp.append(float('inf'))

        for i in range(1,n+1):
            prev = dp[1]
            for j in range(1,n+1):
                tmp = dp[j]
                dp[j] = min(prev, dp[j], dp[j+1]) + mat[i-1][j-1]
                prev = tmp
        return min(dp)

        