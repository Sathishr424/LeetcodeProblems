# Last updated: 10/8/2026, 12:27:19 PM
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        n = len(s)
4
5        open_b = 1
6        ret = ''
7        for i in range(1, n):
8            if s[i] == ')':
9                open_b -= 1
10                if open_b:
11                    ret += s[i]
12            else:
13                if open_b:
14                    ret += s[i]
15                open_b += 1
16
17        return ret