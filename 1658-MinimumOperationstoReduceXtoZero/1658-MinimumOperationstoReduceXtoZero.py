# Last updated: 9/23/2026, 8:11:35 AM
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
11            elif total > x: break
12
13        right = n-1
14        suffix = 0
15        prefix = 0
16        for i in range(n):
17            prefix += nums[i]
18            if prefix > x: break
19
20            while right + 1 < n and prefix + suffix > x:
21                right += 1
22                suffix -= nums[right]
23
24            while right > i and prefix + suffix + nums[right] <= x:
25                suffix += nums[right]
26                right -= 1
27
28            if prefix + suffix == x:
29                best = min(best, i + 1 + (n - right - 1))
30
31        return best if best <= n else -1