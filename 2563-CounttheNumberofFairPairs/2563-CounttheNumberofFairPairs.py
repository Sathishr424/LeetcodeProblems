# Last updated: 28/10/2025, 9:42:57 pm
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        nums.sort()
        pairs = 0

        for i in range(n):
            num = nums[i]

            left = bisect_left(nums, lower - num, lo=i + 1)
            right = bisect_right(nums, upper - num, lo=left)

            pairs += right - left

        return pairs