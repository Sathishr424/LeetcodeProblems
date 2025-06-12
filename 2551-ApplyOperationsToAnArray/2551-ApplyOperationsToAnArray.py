# Last updated: 12/6/2025, 5:37:44 am
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        
        while i < n-1:
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                i += 1
            i += 1
        l = 0

        for i in range(n):
            if nums[i] != 0:
                nums[l] = nums[i]
                l += 1

        while l < n:
            nums[l] = 0
            l += 1

        return nums