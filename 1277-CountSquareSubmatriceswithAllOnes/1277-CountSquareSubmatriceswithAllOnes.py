# Last updated: 20/8/2025, 11:05:34 am
"""
[0,1,1,1,1,1],
[1,1,1,1,1,1],
[0,1,1,1,1,1],
[0,1,1,1,1,1],
[0,1,1,1,1,1]
"""
cmin = lambda x, y: x if x < y else y

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        DIR = [(0, 1), (1, 1), (1, 0)]
        dp = [[0] * (n+1) for _ in range(m+1)]
        tot = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 0: continue
                max_area = inf
                for i2, j2 in DIR:
                    i2 += i
                    j2 += j

                    max_area = cmin(max_area, dp[i2][j2])
                dp[i][j] = max_area + 1
                tot += dp[i][j]
        
        # [print(row) for row in dp]
        return tot