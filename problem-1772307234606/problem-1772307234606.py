# Last updated: 3/1/2026, 1:03:54 AM
1class Solution:
2    def mergeCharacters(self, s: str, k: int) -> str:
3        n = len(s)
4
5        stack = list(s)
6
7        change = True
8        while change:
9            change = False
10            for i in range(len(stack)):
11                for j in range(i+1, len(stack)):
12                    if stack[i] == stack[j] and (j - i) <= k:
13                        stack = stack[:j] + stack[j+1:]
14                        change = True
15                        break
16                if change: break
17
18        return ''.join(stack)
19