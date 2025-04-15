# Last updated: 15/4/2025, 5:30:02 pm
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        ret = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
            
            ret = max(ret, dp[i])
        return ret
