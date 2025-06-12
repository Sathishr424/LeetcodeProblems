# Last updated: 12/6/2025, 5:47:26 am
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix-nums[i] == total-prefix:
                return i
        return -1
