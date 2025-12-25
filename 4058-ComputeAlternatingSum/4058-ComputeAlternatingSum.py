# Last updated: 12/25/2025, 7:08:38 PM
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        alt = True
        s = 0
        for num in nums:
            if alt:
                s += num
            else:
                s -= num
            alt = not alt

        return s