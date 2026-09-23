# Last updated: 9/23/2026, 8:00:53 AM
1class Solution:
2    def minOperations(self, nums: list[int], x: int) -> int:
3        n = len(nums)
4        suffix = [0] * (n + 1)
5        total = 0
6        best = n + 1
7        for i in range(n-1, -1, -1):
8            total += nums[i]
9            suffix[n-i] = total
10            if total == x: best = min(best, n - i)
11
12        total = 0
13        for i in range(n):
14            total += nums[i]
15
16            index = bisect_left(suffix, x - total, hi=n-i)
17            if index < n and suffix[index] + total == x:
18                best = min(best, i + 1 + index)
19
20        return best if best <= n else -1