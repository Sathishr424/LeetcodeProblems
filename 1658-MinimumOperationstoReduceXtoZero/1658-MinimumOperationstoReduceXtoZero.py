# Last updated: 9/23/2026, 8:08:33 AM
1class Solution:
2    def minOperations(self, nums: list[int], x: int) -> int:
3        n = len(nums)
4
5        best = n + 1
6        total = 0
7        for i in range(n-1, -1, -1):
8            total += nums[i]
9            if total == x:
10                best = min(best, n - i)
11
12        right = n-1
13        suffix = 0
14        prefix = 0
15        for i in range(n):
16            prefix += nums[i]
17
18            while right + 1 < n and prefix + suffix > x:
19                right += 1
20                suffix -= nums[right]
21
22            while right > i and prefix + suffix + nums[right] <= x:
23                suffix += nums[right]
24                right -= 1
25
26            if prefix + suffix == x:
27                best = min(best, i + 1 + (n - right - 1))
28
29        return best if best <= n else -1