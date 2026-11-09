# Last updated: 11/9/2026, 11:00:51 PM
1class Solution:
2    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
3        n = len(types)
4        m = len(groupSize)
5
6        stack = []
7        for t, c in zip(types, colors):
8            if stack and stack[-1][0] == t and stack[-1][1] == c:
9                stack.append((t, c, stack.pop()[-1] + 1))
10            else:
11                stack.append((t, c, 1))
12
13            if stack and groupSize[stack[-1][0]] == stack[-1][-1]:
14                stack.pop()
15
16        return len(stack) == 0