# Last updated: 16/7/2025, 12:22:15 pm
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ret = 0
        for add in range(2):
            dp = [0, 0]
            for num in nums:
                curr = num % 2
                need = (curr - add) % 2
                dp[curr] = dp[need] + 1
            
            ret = max(ret, max(dp))
        
        return ret