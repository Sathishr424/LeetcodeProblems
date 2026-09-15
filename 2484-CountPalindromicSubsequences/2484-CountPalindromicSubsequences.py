# Last updated: 9/15/2026, 4:25:42 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n = len(s)
4
5        dp = [[False] * n for _ in range(n + 1)]
6        for k in range(2):
7            for i in range(n):
8                dp[k][i] = True
9
10        best = [0, 0]
11        for k in range(2, n + 1):
12            for i in range(k-1, n):
13                dp[k][i] = s[i] == s[i-k+1] and dp[k-2][i-1]
14                if dp[k][i] and k > best[1] - best[0] + 1:
15                    best = [i-k+1, i]
16
17        return s[best[0]:best[1] + 1]