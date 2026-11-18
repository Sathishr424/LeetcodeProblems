# Last updated: 11/18/2026, 2:13:37 PM
1class Solution:
2    def minChanges(self, s: str) -> int:
3        n = len(s)
4
5        ans = 0
6        one = 0
7        zero = 0
8        for i in range(n):
9            if s[i] == '1':
10                one += 1
11            else:
12                zero += 1
13
14            if i % 2:
15                curr = min(one, zero)
16                ans += curr
17                one = 0
18                zero = 0
19
20        return ans