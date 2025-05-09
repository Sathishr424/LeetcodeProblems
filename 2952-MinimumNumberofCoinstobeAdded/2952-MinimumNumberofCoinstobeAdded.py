# Last updated: 9/5/2025, 3:08:18 pm
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [-float('inf') for _ in range(target+1)]
        dp[0] = 0

        # [0, 1, 1, 2, 1, 1, 2, 2]
        
        for i, num in enumerate(nums):
            prev = dp + []
            for t in range(target):
                if t+num <= target:
                    dp[t+num] = max(prev[t+num], prev[t] + 1)
            # print(dp)
                    
        return dp[target] if dp[target] != -float('inf') else -1
