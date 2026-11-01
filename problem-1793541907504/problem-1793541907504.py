# Last updated: 11/1/2026, 7:35:07 PM
1class Solution:
2    def minMergedInteger(self, nums: list[int]) -> int:
3        n = len(nums)
4
5        best = 10**20
6        for i in range(0, n-1, 2):
7            curr = nums[i]
8            next = nums[i + 1]
9
10            best = min(best, int(str(curr) + str(next)))
11
12        return best