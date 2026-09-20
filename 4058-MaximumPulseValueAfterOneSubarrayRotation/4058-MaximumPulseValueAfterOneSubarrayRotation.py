# Last updated: 9/20/2026, 8:56:59 PM
1class Solution:
2    def maxValue(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        alt_sum = []
6        alt_alt_sum = []
7        for i, num in enumerate(nums):
8            if i % 2:
9                alt_sum.append(-num)
10                alt_alt_sum.append(num)
11            else:
12                alt_sum.append(num)
13                alt_alt_sum.append(-num)
14
15        inf = 10**20
16        @cache
17        def rec(index, alt, used):
18            if index == n:
19                if alt: return -inf
20                return 0
21
22            if not alt:
23                ans = rec(index + 1, alt, used) + alt_sum[index]
24                if not used:
25                    if index + 2 < n: ans = max(ans, rec(index + 2, True, True) + alt_sum[index] + alt_alt_sum[index + 1])
26                    ans = max(ans, rec(index + 1, True, True) + -alt_sum[index])
27            else:
28                ans = rec(index + 2, alt, used) + alt_alt_sum[index] + alt_alt_sum[index + 1] if index + 2 < n else -inf
29                ans = max(ans, rec(index + 1, False, used) + (-alt_sum[index]))
30
31            return ans
32
33        ans = rec(0, False, False)
34        rec.cache_clear()
35
36        return ans