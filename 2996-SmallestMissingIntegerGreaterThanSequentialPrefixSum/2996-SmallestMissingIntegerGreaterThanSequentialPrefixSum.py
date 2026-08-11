# Last updated: 8/11/2026, 6:17:33 PM
1class Solution:
2    def missingInteger(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        there = set(nums)
6        s = nums[0]
7        for i in range(1, n):
8            if nums[i] == nums[i-1] + 1:
9                s += nums[i]
10            else:
11                break
12
13        while s in there:
14            s += 1
15
16        return s