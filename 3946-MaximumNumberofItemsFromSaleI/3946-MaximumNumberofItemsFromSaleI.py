# Last updated: 11/27/2026, 12:48:28 PM
1class Solution:
2    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
3        n = len(items)
4        free = [0] * n
5
6        for i in range(n):
7            for j in range(n):
8                if i == j: continue
9                if items[j][0] % items[i][0] == 0:
10                    free[i] += 1
11
12        dp = [[[0] * 2 for _ in range(budget + 1)] for _ in range(n + 1)]
13        ans = 0
14
15        for i in range(n):
16            item = items[i]
17            for b in range(budget, -1, -1):
18                if b >= item[1]:
19                    dp[i + 1][b - item[1]][0] = max(dp[i + 1][b - item[1]][0], dp[i][b][0] + free[i] + 1, dp[i][b][1] + 1)
20                    dp[i][b - item[1]][1] = max(dp[i][b - item[1]][1], dp[i][b][0] + free[i] + 1, dp[i][b][1] + 1)
21                dp[i + 1][b][0] = max(dp[i + 1][b][0], dp[i][b][0], dp[i][b][1])
22                ans = max(ans, dp[i][b][0], dp[i][b][1])
23
24        # [print(row) for row in dp]
25        return ans