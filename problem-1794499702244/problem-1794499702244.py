# Last updated: 11/12/2026, 9:38:22 PM
1class Solution:
2    def maxAlternatingSum(self, nums: list[int]) -> int:
3        inf = 10**20
4        n = len(nums)
5        # 1 -> index, 2 -> is_alternating, 3 -> did we already used the delete operation
6
7        @cache
8        def rec(index, is_alt, used):
9            if index == n: return 0
10            ans = 0
11            if not used:
12                ans = max(ans, rec(index + 1, is_alt, True))
13
14            curr = 0
15            if is_alt:
16                curr -= nums[index]
17            else:
18                curr += nums[index]
19
20            return max(ans, rec(index + 1, not is_alt, used) + curr)
21
22        best = -inf
23        for i in range(n):
24            best = max(rec(i + 1, True, False) + nums[i], best)
25
26        rec.cache_clear()
27        return best