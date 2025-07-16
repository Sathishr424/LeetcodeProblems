# Last updated: 16/7/2025, 11:55:29 am
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        ret = 0
        for add in range(2):
            dp = [0, 0]
            for i in range(n):
                curr = nums[i] % 2
                need = (2 - curr - add) % 2
                dp[curr] = dp[need] + 1
            
            ret = max(ret, max(dp))
        
        return ret