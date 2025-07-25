# Last updated: 12/6/2025, 5:44:47 am
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ret = 0
        for i in range(n-3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        
        return 0


        
