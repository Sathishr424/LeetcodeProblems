# Last updated: 9/15/2026, 4:38:14 PM
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
18        # [print(i, row) for i, row in enumerate(palindrome)]
19        @cache
20        def rec(index):
21            if index == n: return 0
22
23            ans = rec(index + 1)
24            for right in palindrome[index]:
25                ans = max(ans, rec(right + 1) + 1)
26
27            return ans
28
29        ans = rec(0)
30        rec.cache_clear()
31        return ans