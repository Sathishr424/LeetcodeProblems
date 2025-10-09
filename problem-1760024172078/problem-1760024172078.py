# Last updated: 9/10/2025, 9:06:12 pm
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = sum(nums)
        d_sum = 0

        for num in nums:
            while num:
                d_sum += num % 10
                num //= 10

        return abs(d_sum - s)