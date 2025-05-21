# Last updated: 21/5/2025, 6:30:20 am
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        rows = {}
        cols = {}

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        
        for row in rows:
            for j in range(n):
                matrix[row][j] = 0
        
        for col in cols:
            for i in range(m):
                matrix[i][col] = 0
