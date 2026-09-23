# Last updated: 9/23/2026, 7:48:36 AM
1class Solution:
2    def minOperations(self, nums: list[int], x: int) -> int:
3        n = len(nums)
4        suffix = defaultdict(int)
5        suffix[0] = 0
6        suf = 0
7        for i in range(n-1, -1, -1):
8            suf += nums[i]
9            suffix[suf] = n - i
10
11        prefix = 0
12        best = n + 1
13        if x in suffix: best = suffix[x]
14        suffix[suf] = n + 1
15
16        for i in range(n):
17            suf -= nums[i]
18            suffix[suf] = n + 1
19
20            prefix += nums[i]
21
22            need = x - prefix
23            if need in suffix:
24                best = min(best, (i + 1) + suffix[need])
25
26        return best if best <= n else -1