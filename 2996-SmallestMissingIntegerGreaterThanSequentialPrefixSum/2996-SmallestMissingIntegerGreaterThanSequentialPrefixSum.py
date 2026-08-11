# Last updated: 8/11/2026, 2:25:02 PM
1class Solution:
2    def missingInteger(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        there = set(nums)
6        prev = nums[0]
7        s = prev
8        for i in range(1, n):
9            if nums[i] == prev + 1:
10                s += nums[i]
11                prev = nums[i]
12            else:
13                break
14
15        while s in there:
16            s += 1
17
18        return s