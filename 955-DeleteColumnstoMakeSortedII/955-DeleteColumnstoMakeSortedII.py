# Last updated: 12/21/2025, 12:21:03 PM
1class Solution:
2    def minDeletionSize(self, strs: List[str]) -> int:
3        n = len(strs)
4        m = len(strs[0])
5        op = 0
6        ok = [[[0] * n for _ in range(n)] for _ in range(m + 1)]
7
8        prev_index = 0
9        for index in range(m):
10            for i in range(1, n):
11                prev = strs[i - 1][index]
12                curr = strs[i][index]
13
14                if ok[prev_index][i-1][i] ==  1 or curr > prev:
15                    ok[index + 1][i-1][i] = 1
16                elif curr == prev:
17                    ok[index + 1][i-1][i] = 0
18                else:
19                    op += 1
20                    break
21            else:
22                prev_index = index + 1
23
24        return op