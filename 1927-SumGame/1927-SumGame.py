# Last updated: 8/25/2026, 2:38:06 PM
1class Solution:
2    def missingMultiple(self, nums: List[int], k: int) -> int:
3        there = set(nums)
4
5        multi = k
6        while multi in there:
7            multi += k
8
9        return multi