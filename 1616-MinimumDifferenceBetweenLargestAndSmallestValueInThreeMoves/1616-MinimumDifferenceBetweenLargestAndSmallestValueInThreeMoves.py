# Last updated: 12/6/2025, 5:41:15 am
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4: return 0
        nums.sort()
        tmp = n-4
        ret = float('inf')
        for i in range(4):
            ret = min(nums[i+tmp] - nums[i], ret)

        return ret