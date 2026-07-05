# Last updated: 7/5/2026, 4:01:52 PM
1class Solution:
2    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
3        m = len(board)
4        n = len(board[0])
5        board[0] = '0' + board[0][1:]
6
7        mod = 10**9 + 7
8        dir = [(-1, 0), (0, -1), (-1, -1)]
9        
10        dp = [[[-1, 0] for _ in range(n)] for _ in range(m)]
11        dp[m-1][n-1] = [0, 1]
12
13        for i in range(m-1, -1, -1):
14            for j in range(n-1, -1, -1):
15                if dp[i][j][0] == -1: continue
16                for i2, j2 in dir:
17                    i2 += i
18                    j2 += j
19
20                    if 0 <= i2 < m and 0 <= j2 < n and board[i2][j2] != 'X':
21                        new_tot = dp[i][j][0] + int(board[i2][j2])
22
23                        if new_tot > dp[i2][j2][0]:
24                            dp[i2][j2][0] = new_tot
25                            dp[i2][j2][1] = dp[i][j][1]
26                        elif new_tot == dp[i2][j2][0]:
27                            dp[i2][j2][1] = (dp[i2][j2][1] + dp[i][j][1]) % mod
28
29        if dp[0][0][0] == -1: return [0, 0]
30        return dp[0][0]