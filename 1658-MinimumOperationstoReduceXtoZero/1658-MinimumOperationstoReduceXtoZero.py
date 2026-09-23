# Last updated: 9/23/2026, 8:09:16 AM
1cmin = lambda x, y: x if x < y else y
2class Solution:
3    def minOperations(self, nums: list[int], x: int) -> int:
4        n = len(nums)
5
6        best = n + 1
7        total = 0
8        for i in range(n-1, -1, -1):
9            total += nums[i]
10            if total == x:
11                best = cmin(best, n - i)
12
13        right = n-1
14        suffix = 0
15        prefix = 0
16        for i in range(n):
17            prefix += nums[i]
18
19            while right + 1 < n and prefix + suffix > x:
20                right += 1
21                suffix -= nums[right]
22
23            while right > i and prefix + suffix + nums[right] <= x:
24                suffix += nums[right]
25                right -= 1
26
27            if prefix + suffix == x:
28                best = cmin(best, i + 1 + (n - right - 1))
29
30        return best if best <= n else -1