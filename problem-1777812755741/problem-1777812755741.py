# Last updated: 5/3/2026, 6:22:35 PM
1class Solution:
2    def minOperations(self, nums: list[int]) -> int:
3        n = len(nums)
4        add = 0
5        for i in range(1, n):
6            nums[i] += add
7            if nums[i] < nums[i-1]:
8                diff = nums[i-1] - nums[i]
9                nums[i] += diff
10                add += diff
11
12        return add