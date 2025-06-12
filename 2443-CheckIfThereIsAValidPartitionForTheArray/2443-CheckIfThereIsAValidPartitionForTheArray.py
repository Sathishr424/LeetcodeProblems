# Last updated: 12/6/2025, 5:38:04 am
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(2, n+1):
            last_two = nums[i-1] - nums[i-2]
            if last_two == 0: dp[i] = dp[i-2]
            if i-3 >= 0 and (last_two == 1 or last_two == 0):
                last_three = nums[i-2] - nums[i-3]
                if last_two == last_three:
                    dp[i] = max(dp[i] , dp[i-3])
        
        return dp[-1]