# Last updated: 16/6/2025, 6:28:43 am
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini = nums[0]
        ret = -1
        for i in range(1, len(nums)):
            if nums[i] < mini:
                mini = nums[i]
            
            if nums[i] > mini:
                ret = max(ret, nums[i] - mini)
        
        return ret