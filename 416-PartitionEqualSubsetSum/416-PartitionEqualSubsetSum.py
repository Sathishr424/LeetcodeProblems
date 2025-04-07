# Last updated: 7/4/2025, 4:01:46 pm
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        half = total // 2

        # Bottom up
        dp = [False] * (half+1)
        dp[0] = True

        for num in nums:
            for tot in range(half-num, -1, -1):
                if dp[tot]:
                    dp[tot+num] = True
                    if tot+num == half: return True

        return dp[half]

        
            
            