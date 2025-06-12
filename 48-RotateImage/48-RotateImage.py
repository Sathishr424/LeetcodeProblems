# Last updated: 12/6/2025, 5:54:30 am
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        half = n//2
        half_col = half + (n % 2 != 0)

        for i in range(half):
            for j in range(half_col):
                tmp = matrix[i][j]
                for k in range(4):
                    i, j = j, n - (i+1)
                    matrix[i][j], tmp = tmp, matrix[i][j]
        