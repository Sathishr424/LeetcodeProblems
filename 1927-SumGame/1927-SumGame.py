# Last updated: 8/25/2026, 2:35:42 PM
1class Solution:
2    def stoneGameVIII(self, stones: List[int]) -> int:
3        n = len(stones)
4
5        prefix = [0]
6        for stone in stones:
7            prefix.append(prefix[-1] + stone)
8
9        @cache
10        def rec(index, alice):
11            if index == n-1:
12                return prefix[index + 1] * (1 if alice else -1)
13
14            ans = rec(index + 1, alice)
15            if alice:
16                return max(ans, rec(index + 1, alice ^ 1) + prefix[index + 1])
17            else:
18                return min(ans, rec(index + 1, alice ^ 1) - prefix[index + 1])
19
20        ans = rec(1, 1)
21        rec.cache_clear()
22        return ans