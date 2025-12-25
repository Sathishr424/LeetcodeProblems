# Last updated: 12/25/2025, 7:09:13 PM
class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ret |= nums[i]

        return ret