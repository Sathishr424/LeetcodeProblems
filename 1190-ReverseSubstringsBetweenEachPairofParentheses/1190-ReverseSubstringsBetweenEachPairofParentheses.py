# Last updated: 9/27/2026, 1:19:34 PM
1class Solution:
2    def reverseParentheses(self, s: str) -> str:
3        n = len(s)
4
5        pairs = [-1] * n
6
7        open = []
8        for i in range(n):
9            if s[i] == '(':
10                open.append(i)
11            elif s[i] == ')':
12                pairs[open.pop()] = i
13
14        def rec(l, r):
15            i = l
16            curr = ''
17            while i <= r:
18                if s[i] == '(':
19                    curr += rec(i + 1, pairs[i] - 1)[::-1]
20                    i = pairs[i]
21                else:
22                    curr += s[i]
23                i += 1
24
25            return curr
26
27        return rec(0, n-1)