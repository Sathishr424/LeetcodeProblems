# Last updated: 8/25/2026, 2:32:03 PM
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
12                if alice:
13                    return prefix[index + 1]
14                else:
15                    return -prefix[index + 1]
16
17            ans = rec(index + 1, alice)
18            if alice:
19                ans = max(ans, rec(index + 1, not alice) + prefix[index + 1])
20            else:
21                ans = min(ans, rec(index + 1, not alice) - prefix[index + 1])
22
23            return ans
24
25        ans = rec(1, True)
26        rec.cache_clear()
27        return ans