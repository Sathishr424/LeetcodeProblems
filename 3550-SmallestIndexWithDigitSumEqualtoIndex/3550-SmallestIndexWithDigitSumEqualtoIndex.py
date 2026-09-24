# Last updated: 9/24/2026, 7:02:27 PM
1class Solution:
2    def smallestIndex(self, nums: List[int]) -> int:
3        for i, num in enumerate(nums):
4            s = 0
5            while num:
6                s += num % 10
7                num //= 10
8            if s == i: return i
9
10        return -1