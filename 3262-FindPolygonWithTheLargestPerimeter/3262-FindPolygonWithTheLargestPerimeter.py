# Last updated: 12/6/2025, 5:35:56 am
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ret = -1
        prefix = sum(nums[:2])
        for i in range(2, len(nums)):
            if prefix > nums[i]:
                ret = prefix+nums[i]
            prefix += nums[i]
        
        return ret