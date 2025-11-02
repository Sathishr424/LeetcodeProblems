# Last updated: 2/11/2025, 8:08:45 am
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = 10 ** 5
        n = len(nums)
        nums.sort()

        mid = abs(nums[0] * nums[-1])
        left = abs(nums[0] * nums[1])
        right = abs(nums[-1] * nums[-2])

        return max(left, mid, right) * N