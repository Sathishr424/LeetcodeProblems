# Last updated: 11/10/2026, 3:14:38 PM
1class Solution:
2    def climbStairs(self, n: int, costs: List[int]) -> int:
3        dp = [inf] * (n + 1)
4        dp[0] = 0
5        for i in range(1, n + 1):
6            dp[i] = dp[i-1] + costs[i-1] + 1
7            if i - 2 >= 0:
8                dp[i] = min(dp[i], costs[i-1] + dp[i-2] + 4)
9
10            if i - 3 >= 0:
11                dp[i] = min(dp[i], costs[i-1] + dp[i-3] + 9)
12        return dp[n]