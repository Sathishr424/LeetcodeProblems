# Last updated: 28/10/2025, 8:00:44 pm
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        nums.sort()
        # print(nums)
        pairs = 0

        for i in range(n):
            num = nums[i]

            left = bisect_left(nums, lower - num, lo=i + 1)
            right = bisect_right(nums, upper - num, lo=left)
            # print(num, (left, right))

            pairs += right - left

        return pairs