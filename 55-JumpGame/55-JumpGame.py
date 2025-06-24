# Last updated: 25/6/2025, 12:03:44 am
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [0] * n
        larger = 0

        for i in range(n):
            if i <= larger:
                larger = max(larger, i + nums[i])
            else:
                return False
        
        return True
