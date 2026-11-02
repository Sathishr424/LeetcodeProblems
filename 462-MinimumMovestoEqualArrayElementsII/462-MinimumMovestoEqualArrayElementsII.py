# Last updated: 11/2/2026, 4:34:19 PM
1class Solution:
2    def minMoves2(self, nums: list[int]) -> int:
3        n = len(nums)
4        nums.sort()
5        ans = 0
6        mid = nums[n // 2]
7        for num in nums:
8            ans += abs(num - mid)
9        return ans