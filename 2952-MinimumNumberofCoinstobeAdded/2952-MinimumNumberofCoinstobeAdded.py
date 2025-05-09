# Last updated: 9/5/2025, 3:19:36 pm
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        dp = [-float('inf') for _ in range(target+1)]
        dp[0] = 0
        
        for i, num in enumerate(nums):
            prev = dp + []
            for t in range(target):
                if t+num > target: break
                dp[t+num] = max(prev[t+num], prev[t] + 1)
                    
        return dp[target] if dp[target] != -float('inf') else -1
