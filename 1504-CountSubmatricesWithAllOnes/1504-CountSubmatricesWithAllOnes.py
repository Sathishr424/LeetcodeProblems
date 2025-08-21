# Last updated: 21/8/2025, 11:10:45 pm
class Solution:
    def numSubmat(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        v = [[0] * n for _ in range(m)]

        for j in range(n):
            for i in range(m):
                if matrix[i][j] == 1:
                    v[i][j] = v[i - 1][j] + 1

        count = 0
        for i in range(m):
            stack = []
            for j in range(n):
                h = v[i][j]
                count += h
                for k in range(j + 1, n):
                    h = min(h, v[i][k])
                    count += h
            
        return count