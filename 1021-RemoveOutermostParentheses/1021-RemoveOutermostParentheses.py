# Last updated: 10/8/2026, 12:24:49 PM
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        n = len(s)
4
5        stack = [0]
6        ret = ''
7        for i in range(1, n):
8            if s[i] == ')':
9                stack.pop()
10                if len(stack):
11                    ret += s[i]
12            else:
13                if len(stack):
14                    ret += s[i]
15                stack.append(i)
16
17        return ret