# Last updated: 12/6/2025, 5:36:13 am
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums.sort()

        dp = [-1 for _ in range(target+1)]
        dp[0] = 0

        for i, num in enumerate(nums):
            for t in range(target-num, -1, -1):
                if dp[t] >= 0 and dp[t] + 1 > dp[t+num]:
                    dp[t+num] = dp[t] + 1
        
        return dp[target]