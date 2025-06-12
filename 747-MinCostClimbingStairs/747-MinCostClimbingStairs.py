# Last updated: 12/6/2025, 5:47:08 am
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+2)

        for i in range(n-1, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        
        return min(dp[0], dp[1])