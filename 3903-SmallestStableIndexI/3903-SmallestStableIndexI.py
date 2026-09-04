# Last updated: 9/4/2026, 10:00:35 AM
1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4
5        suffix_min = [nums[-1]] * (n + 1)
6        for i in range(n-1, -1, -1):
7            suffix_min[i] = min(nums[i], suffix_min[i + 1])
8
9        left = nums[0]
10        for i in range(n):
11            left = max(left, nums[i])
12            right = suffix_min[i]
13
14            if left - right <= k:
15                return i
16
17        return -1