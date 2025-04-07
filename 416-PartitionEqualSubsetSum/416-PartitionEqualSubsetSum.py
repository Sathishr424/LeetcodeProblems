# Last updated: 7/4/2025, 3:56:02 pm
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        half = total // 2
        dp = {}
        dp[0] = True

        for num in nums:
            for tot in list(dp.keys()):
                dp[tot+num] = True

        return half in dp

        
            
            