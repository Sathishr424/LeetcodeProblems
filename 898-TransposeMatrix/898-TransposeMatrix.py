# Last updated: 12/6/2025, 5:45:52 am
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        ret = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                ret[i][j] = matrix[j][i]
        
        return ret