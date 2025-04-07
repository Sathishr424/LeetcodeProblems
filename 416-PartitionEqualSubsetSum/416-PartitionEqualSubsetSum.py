# Last updated: 7/4/2025, 3:50:06 pm
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        half = total // 2
        dp = [False] * (half+1)
        dp[0] = True

        for num in nums:
            for tot in range(half-1, -1, -1):
                if dp[tot] and tot+num <= half:
                    dp[tot+num] = True

        return dp[half]

        
            
            