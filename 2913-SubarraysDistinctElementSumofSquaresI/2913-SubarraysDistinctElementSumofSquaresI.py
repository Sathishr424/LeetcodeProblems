# Last updated: 10/15/2026, 6:47:34 PM
1class Solution:
2    def sumCounts(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        ans = 0
6        for i in range(n):
7            uniq = set()
8            for j in range(i, n):
9                uniq.add(nums[j])
10                ans += len(uniq) ** 2
11
12        return ans