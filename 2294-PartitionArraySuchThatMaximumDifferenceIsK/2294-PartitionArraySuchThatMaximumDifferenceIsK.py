# Last updated: 19/6/2025, 5:44:47 am
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)
        ret = 0
        i = 0
        while i < n:
            s = i
            while i < n and nums[i] - nums[s] <= k:
                i += 1
            ret += 1
        
        return ret