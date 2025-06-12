# Last updated: 12/6/2025, 5:52:49 am
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [float('inf')] * (n+1)
        dp[1] = 0
        for i in range(1, n+1):
            tmp = dp[0]
            for j in range(1, i+1):
                curr = dp[j]
                dp[j] = min(dp[j], tmp) + triangle[i-1][j-1]
                tmp = curr
        return min(dp)
