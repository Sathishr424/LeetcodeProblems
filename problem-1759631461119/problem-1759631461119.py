# Last updated: 5/10/2025, 8:01:01 am
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