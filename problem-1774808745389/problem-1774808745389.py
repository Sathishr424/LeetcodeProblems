# Last updated: 3/29/2026, 11:55:45 PM
1class Solution:
2    def minAbsoluteDifference(self, nums: list[int]) -> int:
3        n = len(nums)
4
5        one = -inf
6        two = -inf
7        best = inf
8
9        for i in range(n):
10            if nums[i] == 1:
11                best = min(best, i - two)
12                one = i
13            elif nums[i] == 2:
14                best = min(best, i - one)
15                two = i
16                
17        return -1 if best == inf else best