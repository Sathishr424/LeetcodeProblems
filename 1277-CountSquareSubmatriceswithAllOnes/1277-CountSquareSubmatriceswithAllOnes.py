# Last updated: 20/8/2025, 11:06:35 am
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
        tot = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 0: continue
                max_area = inf
                for i2, j2 in DIR:
                    i2 += i
                    j2 += j

                    max_area = cmin(max_area, matrix[i2][j2] if i2 < m and j2 < n else 0)
                matrix[i][j] = max_area + 1
                tot += matrix[i][j]
        
        return tot