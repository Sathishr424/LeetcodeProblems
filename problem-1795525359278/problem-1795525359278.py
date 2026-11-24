# Last updated: 11/24/2026, 6:32:39 PM
1class Solution:
2    def minCost(self, nums: list[int]) -> int:
3        n = len(nums)
4
5        suffix = [0] * n
6        for i in range(n-2, -1, -1):
7            if nums[i] == nums[i + 1]:
8                suffix[i] = suffix[i+1] + 1
9
10        best = inf
11        left = 0
12        for i in range(1, n-1):
13            if nums[i] == nums[i-1]: left += 1
14            else: left = 0
15
16            right = suffix[i]
17
18            best = min(best, (i-left) * nums[i] + nums[i] * (n-i-1-right))
19
20        return best