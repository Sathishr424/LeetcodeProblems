# Last updated: 11/14/2026, 4:47:40 PM
1class Solution:
2    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
3        n = len(nums)
4        best = inf
5
6        for i in range(n):
7            curr = 0
8            for j in range(i, min(n, i + r)):
9                curr += nums[j]
10                if curr > 0 and j - i + 1 >= l:
11                    best = min(best, curr)
12
13        return -1 if best == inf else best
14