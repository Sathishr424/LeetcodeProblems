# Last updated: 16/6/2025, 6:30:40 am
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini = nums[0]
        ret = 0
        for i in range(1, len(nums)):
            if nums[i] < mini:
                mini = nums[i]
            
            ret = max(ret, nums[i] - mini)
        
        return -1 if ret == 0 else ret