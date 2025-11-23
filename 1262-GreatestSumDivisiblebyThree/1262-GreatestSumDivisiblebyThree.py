# Last updated: 23/11/2025, 5:56:11 am
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[-inf] * (n + 1) for _ in range(3)]
        dp[0][0] = 0

        for i in range(n):
            for rem in range(3):
                dp[rem][i + 1] = max(dp[rem][i + 1], dp[rem][i])

                new_rem = (rem + nums[i]) % 3
                dp[new_rem][i + 1] = max(dp[new_rem][i + 1], dp[rem][i] + nums[i])
        
        return dp[0][n]