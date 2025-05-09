# Last updated: 9/5/2025, 3:43:25 pm
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