# Last updated: 11/7/2026, 8:14:15 PM
1class Solution:
2    def countValidSubstrings(self, s: str) -> int:
3        n = len(s)
4
5        ans = 0
6        prev = 0
7        for i in range(2, n):
8            if s[i-2] == 'a' and s[i-1] == 'b' and s[i] == 'c':
9                left = i - prev
10                # print(i, left)
11                ans += left * (left + 1) // 2 - 1
12                prev = i - 1
13                if i == n-1: return ans + 3
14
15        left = n - prev
16        ans += left * (left + 1) // 2
17        return ans