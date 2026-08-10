# Last updated: 8/10/2026, 2:09:41 PM
1squares = []
2num = 1
3N = 10**5
4while num * num <= N:
5    squares.append(num * num)
6    num += 1
7
8dp = [[True, False] for _ in range(N+1)]
9
10for rem in range(N + 1):
11    for alice in range(2):
12        opp = 0 if alice else 1
13        for num in squares:
14            if rem + num > N: break
15            if alice:
16                dp[rem + num][opp] = dp[rem + num][opp] and dp[rem][alice]
17            else:
18                dp[rem + num][opp] = dp[rem + num][opp] or dp[rem][alice]
19
20class Solution:
21    def winnerSquareGame(self, n: int) -> bool:
22        return dp[n][1]
23