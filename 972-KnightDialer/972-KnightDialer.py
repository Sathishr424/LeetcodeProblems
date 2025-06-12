# Last updated: 12/6/2025, 5:45:07 am
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        mod = (10 ** 9) + 7
        memo = [
            [4, 6], # 0
            [6, 8], # 1
            [9, 7], # 2
            [4, 8], # 3
            [9, 3, 0], # 4
            [], # 5
            [7, 1, 0], # 6
            [2, 6], # 7
            [1, 3], # 8
            [4, 2] # 9
        ]

        dp = [[0] * 10 for _ in range(n-1)]
        for i in range(10):
            dp[n-2][i] += len(memo[i])

        for i in range(n-3, -1, -1):
            for j in range(10):
                for k in memo[j]:
                    dp[i][j] += dp[i+1][k]
            dp.pop()

        return sum(dp[0]) % mod
            