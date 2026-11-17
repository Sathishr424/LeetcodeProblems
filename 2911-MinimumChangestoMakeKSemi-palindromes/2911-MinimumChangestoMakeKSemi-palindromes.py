# Last updated: 11/17/2026, 3:04:27 PM
1N = 201
2divisors = [[] for _ in range(N)]
3for m in range(N):
4    for d in range(2, m//2 + 1):
5        if m % d == 0:
6            divisors[m].append(d)
7
8class Solution:
9    def minimumChanges(self, s: str, k: int) -> int:
10        n = len(s)
11        inf = 10**20
12
13        def getSemiPalindromeChanges(l, d, window, best):
14            change = 0
15            for i in range(d):
16                for j in range(window//2):
17                    if s[l + i + (j * d)] != s[l + i + ((window - j - 1) * d)]:
18                        change += 1
19                        if change >= best: return best
20            return change
21
22        @cache
23        def getMinChanges(l, r):
24            m = r - l + 1
25            best = 0
26            for i in range(l, l + m//2):
27                if s[i] != s[r-(i-l)]:
28                    best += 1
29            
30            for d in divisors[m]:
31                if best == 0: break
32                best = getSemiPalindromeChanges(l, d, m // d, best)
33            
34            return best
35
36        @cache
37        def rec(index, rem):
38            if rem == 1: return getMinChanges(index, n-1)
39
40            ans = inf
41            for i in range(index + 1, n - ((rem - 1) * 2)):
42                ans = min(ans, rec(i + 1, rem - 1) + getMinChanges(index, i))
43
44            return ans
45
46        ans = rec(0, k)
47        rec.cache_clear()
48        getMinChanges.cache_clear()
49        return ans