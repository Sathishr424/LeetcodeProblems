# Last updated: 27/4/2025, 2:32:56 pm
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)-2):
            ret += nums[i] + nums[i+2] == nums[i+1] / 2
        # a + c == b/2   
        return ret