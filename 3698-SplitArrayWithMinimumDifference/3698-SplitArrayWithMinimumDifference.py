# Last updated: 28/9/2025, 11:39:11 am
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)

        s = sum(nums)

        left = [0] * n
        left[0] = 1
        right = [0] * n
        right[-1] = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left[i] = 1
            else:
                break

        for i in range(n-2, -1, -1):
            if nums[i] > nums[i + 1]:
                right[i] = 1
            else:
                break

        min_diff = inf
        curr = 0
        for i in range(n-1):
            curr += nums[i]
            s -= nums[i]
            if left[i] and right[i + 1]:
                min_diff = min(min_diff, abs(curr - s))

        return -1 if min_diff == inf else min_diff