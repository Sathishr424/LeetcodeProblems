# Last updated: 7/4/2025, 4:03:11 pm
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        half = total // 2

        # Bottom up
        dp = {}
        dp[0] = True

        for num in nums:
            new_dp = {}
            for tot in dp:
                new_dp[tot] = True
                new_dp[tot+num] = True
                if tot+num == half: return True
            dp = new_dp

        return half in dp

        
            
            