# Last updated: 12/6/2025, 5:50:54 am
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        zero = 0

        while zero < n and nums[zero] != 0:
            zero += 1
        
        for i in range(zero+1, n):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], 0
                zero += 1