# Last updated: 12/6/2025, 5:44:54 am
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        half = n//2
        for i in range(half):
            if nums[i] == nums[half+i]: return nums[i]
        
        for i in range(1, half+1):
            if nums[i] == nums[i-1]: return nums[i]
        
        return nums[n-1]
