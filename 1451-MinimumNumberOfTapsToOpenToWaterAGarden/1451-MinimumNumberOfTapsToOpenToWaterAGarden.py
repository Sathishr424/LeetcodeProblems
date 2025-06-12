# Last updated: 12/6/2025, 5:42:18 am
class Solution:
    def minTaps(self, n: int, ranges) -> int:
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(n+1):
            left = max(0, i-ranges[i])
            right = min(n, i+ranges[i])

            for j in range(left, right+1):
                dp[right] = min(dp[right], dp[j]+1)

        return -1 if dp[j] == float('inf') else dp[n]