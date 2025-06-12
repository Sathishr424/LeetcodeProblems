# Last updated: 12/6/2025, 5:54:21 am
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left = nums[0]
        for i in range(1, len(nums)):
            if left >= i:
                left = max(left, i+nums[i])
            else: return False
        
        return True