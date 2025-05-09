# Last updated: 9/5/2025, 3:27:02 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        dp = [-float('inf') for _ in range(target+1)]
        prev = [-float('inf') for _ in range(target+1)]
        dp[0] = 0
        
        for i, num in enumerate(nums):
            dp, prev = prev, dp

            for t in range(target):
                if t+num > target: break

                dp[t] = cmax(dp[t], prev[t])
                dp[t+num] = cmax(prev[t+num], prev[t] + 1) 

        return cmax(-1, cmax(dp[target], prev[target]))