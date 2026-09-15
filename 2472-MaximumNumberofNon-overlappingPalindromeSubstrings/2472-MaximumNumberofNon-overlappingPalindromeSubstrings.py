# Last updated: 9/15/2026, 4:54:53 PM
1class Solution:
2    def maxPalindromes(self, s: str, k: int) -> int:
3        def check(l: int, r: int) -> bool:
4            while l < r:
5                if s[l] != s[r]:
6                    return False
7                l += 1
8                r -= 1
9            return True
10
11        n = len(s)
12        ans = 0
13        start = 0
14
15        for r in range(k - 1, n):
16            l = r - k + 1
17            if l >= start and check(l, r):
18                ans += 1
19                start = r + 1
20                continue
21
22            l = r - k
23            if l >= start and check(l, r):
24                ans += 1
25                start = r + 1
26
27        return ans