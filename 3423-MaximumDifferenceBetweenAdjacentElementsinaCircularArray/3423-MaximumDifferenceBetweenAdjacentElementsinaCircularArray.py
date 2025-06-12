# Last updated: 12/6/2025, 5:35:14 am
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)

        ret = 0
        for i in range(n-1):
            ret = max(ret, abs(nums[i] - nums[i+1]))
        
        return max(ret, abs(nums[0] - nums[-1]))