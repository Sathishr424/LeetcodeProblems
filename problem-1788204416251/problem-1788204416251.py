# Last updated: 9/1/2026, 12:56:56 AM
1class Solution:
2    def maxPairStrength(self, nums: list[int]) -> int:
3        n = len(nums)
4
5        best = (nums[0] * nums[1]) / pow(gcd(nums[0], nums[1]), 2)
6        for i in range(n):
7            for j in range(i + 1, n):
8                best = max(best, (nums[i] * nums[j]) / pow(gcd(nums[i], nums[j]), 2))
9
10        return int(best)