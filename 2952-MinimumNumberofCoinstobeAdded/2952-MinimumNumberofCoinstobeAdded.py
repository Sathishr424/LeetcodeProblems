# Last updated: 9/5/2025, 3:32:52 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        dp = [-float('inf') for _ in range(target+1)]
        dp[0] = 0

        for i, num in enumerate(nums):
            for t in range(target-num, -1, -1):
                dp[t+num] = cmax(dp[t+num], dp[t] + 1)
        
        return cmax(-1, dp[target])