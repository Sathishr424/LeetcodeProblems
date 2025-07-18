# Last updated: 12/6/2025, 5:45:31 am
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(1, len(nums)):
            inc = inc and nums[i-1] >= nums[i]
            dec = dec and nums[i-1] <= nums[i]
        return inc or dec