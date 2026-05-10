# Last updated: 5/10/2026, 7:01:32 PM
1class Solution:
2    def concatWithReverse(self, nums: list[int]) -> list[int]:
3        return nums + nums[::-1]