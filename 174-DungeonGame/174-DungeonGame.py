# Last updated: 26/7/2025, 2:49:09 am
class Solution:
    def calculateMinimumHP(self, dung: List[List[int]]) -> int:
        m = len(dung)
        n = len(dung[0])

        def isGood(health):
            dp = [[-inf] * n for _ in range(m)]
            dp[0][0] = health
            for i in range(m):
                for j in range(n):
                    dp[i][j] += dung[i][j]
                    if dp[i][j] <= 0: dp[i][j] = -inf
                    if i + 1 < m:
                        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
                    if j + 1 < n:
                        dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])

            return dp[m-1][n-1] > 0
        
        l = 1
        r = 1

        for i in range(m):
            for j in range(n):
                if dung[i][j] < 0:
                    r += -dung[i][j]

        while l < r:
            mid = (l + r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1
        
        return l