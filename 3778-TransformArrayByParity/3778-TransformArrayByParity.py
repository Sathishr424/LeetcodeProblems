# Last updated: 12/6/2025, 5:34:24 am
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        return sorted(nums)