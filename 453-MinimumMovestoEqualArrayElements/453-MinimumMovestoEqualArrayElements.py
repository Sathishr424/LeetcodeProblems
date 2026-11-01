# Last updated: 11/1/2026, 4:03:04 PM
1class Solution:
2    def minMoves(self, nums: list[int]) -> int:
3        mn = min(nums)
4        return sum([num - mn for num in nums])