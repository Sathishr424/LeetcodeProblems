# Last updated: 11/18/2026, 3:39:09 PM
1class Solution:
2    def minChanges(self, s: str) -> int:
3        n = len(s)
4        ans = 0
5
6        for i in range(0, n, 2):
7            one = int(s[i]) + int(s[i+1])
8            ans += min(one, 2 - one)
9        
10        return ans
11