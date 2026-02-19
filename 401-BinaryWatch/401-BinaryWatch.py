# Last updated: 2/19/2026, 1:52:43 PM
1class Solution:
2    def countBinarySubstrings(self, s: str) -> int:
3        n = len(s)
4
5        ans = 0
6        cnt = 1
7        prev = 0
8        for i in range(1, n):
9            if s[i] == s[i - 1]:
10                cnt += 1
11            else:
12                ans += min(cnt, prev)
13                prev = cnt
14                cnt = 1
15            
16        ans += min(prev, cnt)
17        return ans