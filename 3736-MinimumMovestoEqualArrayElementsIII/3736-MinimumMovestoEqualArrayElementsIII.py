# Last updated: 11/3/2026, 11:38:46 AM
1class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        mx = max(nums)
4        return sum([mx - num for num in nums])