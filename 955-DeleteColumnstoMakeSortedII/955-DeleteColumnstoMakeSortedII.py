# Last updated: 12/21/2025, 12:14:08 PM
1class Solution:
2    def minDeletionSize(self, strs: List[str]) -> int:
3        n = len(strs)
4        m = len(strs[0])
5        op = 0
6        pair = {}
7        for i in range(n):
8            for j in range(i+1, n):
9                pair[(i, j)] = 0
10
11        for index in range(m):
12            new_pair = {}
13            for i in range(1, n):
14                prev = strs[i - 1][index]
15                curr = strs[i][index]
16
17                if pair[(i-1, i)] ==  1 or curr > prev:
18                    new_pair[(i-1, i)] = 1
19                elif curr == prev:
20                    new_pair[(i-1, i)] = 0
21                else:
22                    op += 1
23                    break
24            else:
25                pair = new_pair
26
27        return op