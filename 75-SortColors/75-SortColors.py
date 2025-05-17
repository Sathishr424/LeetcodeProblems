# Last updated: 17/5/2025, 11:42:55 am
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        
        for i in range(left, n):
            if nums[i] == 1:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1