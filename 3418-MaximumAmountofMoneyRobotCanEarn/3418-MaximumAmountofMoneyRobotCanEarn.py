# Last updated: 4/3/2026, 2:30:34 PM
1from typing import List
2
3inf = 10**20
4class Solution:
5    def maximumAmount(self, coins: List[List[int]]) -> int:
6        m = len(coins)
7        n = len(coins[0])
8
9        dp = [[[-inf] * 3 for _ in range(n)] for _ in range(m)]
10        dp[0][0][2] = coins[0][0]
11        dp[0][0][1] = 0
12        
13        for i in range(m):
14            for j in range(n):
15                for rem in range(2, -1, -1):
16                    if i + 1 < m:
17                        dp[i + 1][j][rem] = max(dp[i + 1][j][rem], dp[i][j][rem] + coins[i + 1][j])
18                        if rem: 
19                            dp[i + 1][j][rem - 1] = max(dp[i + 1][j][rem - 1], dp[i][j][rem])
20                    if j + 1 < n:
21                        dp[i][j + 1][rem] = max(dp[i][j + 1][rem], dp[i][j][rem] + coins[i][j + 1])
22                        if rem: 
23                            dp[i][j + 1][rem - 1] = max(dp[i][j + 1][rem - 1], dp[i][j][rem])
24
25        return max(dp[-1][-1])
26