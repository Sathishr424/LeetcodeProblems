# Last updated: 12/6/2025, 5:35:42 am
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2: return False
        
        return True
