# Last updated: 19/8/2025, 1:11:52 pm
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        ret = 0
        left = 0
        for i in range(n):
            if nums[i] != 0:
                left = i + 1
            
            ret += i - left + 1
        
        return ret