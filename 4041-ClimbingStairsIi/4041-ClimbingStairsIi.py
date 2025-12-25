# Last updated: 12/25/2025, 7:08:55 PM
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [-1] * n
        def rec(curr):
            if curr == n: return 0
            if dp[curr] != -1: return dp[curr]
            
            ans = inf
            for j in range(curr + 1, curr + 4):
                if j > n: break
                ans = min(ans, rec(j) + costs[j - 1] + (j - curr) ** 2)

            dp[curr] = ans
            return ans

        return rec(0)