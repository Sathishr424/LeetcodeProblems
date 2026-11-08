# Last updated: 11/9/2026, 12:29:55 AM
1class Solution:
2    def countSuffix(self, nums: list[int], target: list[int]) -> int:
3        n = len(nums)
4
5        suffix = [0] * n
6        suffix[n-1] = 1
7        for i in range(n-2, -1, -1):
8            if target[i] >= target[i + 1]:
9                suffix[i] = 1
10            else: break
11
12        if sorted(nums) != sorted(target): return 0
13        
14        ans = 0
15        for i in range(n):
16            if suffix[i]: ans += 1
17            if nums[i] != target[i]: break
18
19        return ans