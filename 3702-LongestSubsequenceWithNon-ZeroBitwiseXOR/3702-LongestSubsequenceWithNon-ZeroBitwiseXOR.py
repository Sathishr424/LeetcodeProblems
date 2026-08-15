# Last updated: 8/15/2026, 3:48:55 PM
1class Solution:
2    def longestSubsequence(self, nums: List[int]) -> int:
3        n = len(nums)
4        mx = max(nums)
5
6        for b in range(32):
7            cnt = 0
8            for num in nums:
9                cnt += (num & (1 << b) > 0)
10
11            rem = n - cnt
12            if cnt % 2:
13                return n
14
15        return n-1 if mx > 0 else 0