# Last updated: 11/10/2026, 3:16:58 PM
1class Solution:
2    def climbStairs(self, n: int, costs: List[int]) -> int:
3        dp = [0] * (n + 1)
4        for i in range(1, n + 1):
5            cost = costs[i-1]
6
7            dp[i] = dp[i-1] + cost + 1
8
9            if i - 2 >= 0:
10                dp[i] = min(dp[i], cost + dp[i-2] + 4)
11
12            if i - 3 >= 0:
13                dp[i] = min(dp[i], cost + dp[i-3] + 9)
14
15        return dp[n]