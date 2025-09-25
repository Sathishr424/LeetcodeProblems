# Last updated: 25/9/2025, 12:12:50 pm
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = [0] * n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            prev = dp[0]
            dp[0] += triangle[i][0]
            for j in range(1, i):
                new_prev = dp[j]
                dp[j] = min(dp[j] + triangle[i][j], prev + triangle[i][j])
                prev = new_prev
            dp[i] = prev + triangle[i][i]
        
        return min(dp)