# Last updated: 9/15/2026, 4:55:01 PM
1class Solution:
2    def maxPalindromes(self, s: str, min_length: int) -> int:
3        n = len(s)
4        if min_length == 1: return n
5
6        dp = [[False] * n for _ in range(n + 1)]
7        for k in range(2):
8            for i in range(n):
9                dp[k][i] = True
10
11        palindrome = [[] for _ in range(n)]
12        for k in range(2, n + 1):
13            for i in range(k-1, n):
14                dp[k][i] = s[i] == s[i-k+1] and dp[k-2][i-1]
15                if k >= min_length and dp[k][i]:
16                    palindrome[i-k+1].append(i)
17
18
19        dp_two = [0] * (n+1)
20        for left in range(n):
21            dp_two[left] = max(dp_two[left], dp_two[left - 1])
22            for right in palindrome[left]:
23                dp_two[right + 1] = max(dp_two[right + 1], dp_two[left] + 1)
24
25        return max(dp_two[-1], dp_two[-2])