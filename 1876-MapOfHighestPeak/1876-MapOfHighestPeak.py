# Last updated: 12/6/2025, 5:40:03 am
class Solution:
    def highestPeak(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                mat[i][j] = 1 if mat[i][j] == 0 else 0

        def getVal(x, y):
            if x == -1 or x == m or y == -1 or y == n: return float('inf')
            return mat[x][y]

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = min(getVal(i-1, j), getVal(i, j-1)) + 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] != 0:
                    mat[i][j] = min(mat[i][j], getVal(i+1, j) + 1, getVal(i, j+1) + 1)
        return mat
        