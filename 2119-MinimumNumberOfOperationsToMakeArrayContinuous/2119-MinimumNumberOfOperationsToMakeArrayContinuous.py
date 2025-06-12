# Last updated: 12/6/2025, 5:39:11 am
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))

        ans = n
        for i, start in enumerate(nums):
            end = start + n - 1
            idx = bisect_right(nums, end)
            uniqueLen = idx - i
            ans = min(ans, n - uniqueLen)
        return ans