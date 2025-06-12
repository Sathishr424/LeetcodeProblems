# Last updated: 12/6/2025, 5:51:57 am
class Solution:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = nums[0]

        for i in range(1, len(nums)):
            tmp = second
            second = max(first + nums[i], second)
            first = tmp

        return second