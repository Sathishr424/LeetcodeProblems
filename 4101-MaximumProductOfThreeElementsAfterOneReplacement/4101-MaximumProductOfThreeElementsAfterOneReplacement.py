# Last updated: 12/25/2025, 7:08:12 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = 10 ** 5
        n = len(nums)
        nums.sort()

        mid = abs(nums[0] * nums[-1])
        left = abs(nums[0] * nums[1])
        right = abs(nums[-1] * nums[-2])

        return max(left, mid, right) * N