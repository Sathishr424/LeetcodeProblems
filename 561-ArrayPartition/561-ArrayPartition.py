# Last updated: 12/6/2025, 5:48:23 am
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0

        for i in range(0,len(nums),2):
            ret += nums[i]
        
        return ret
