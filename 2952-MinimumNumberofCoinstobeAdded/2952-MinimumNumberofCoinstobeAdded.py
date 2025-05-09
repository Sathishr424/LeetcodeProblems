# Last updated: 9/5/2025, 3:39:20 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums.sort()

        dp = [-1001 for _ in range(target+1)]
        dp[0] = 0

        for i, num in enumerate(nums):
            for t in range(target-num, -1, -1):
                if dp[t] >= dp[t+num]:
                    dp[t+num] = dp[t] + 1
        
        return max(-1, dp[target])