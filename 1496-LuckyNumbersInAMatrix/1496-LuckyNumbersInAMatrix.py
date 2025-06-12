# Last updated: 12/6/2025, 5:42:00 am
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ret = []
        m = len(matrix)
        n = len(matrix[0])

        rows = defaultdict(list)

        for i in range(n):
            col = 0
            for j in range(1, m):
                if matrix[j][i] > matrix[col][i]:
                    col = j
            rows[col].append(i)

        for i in rows:
            row = 0
            for j in range(1, n):
                if matrix[i][j] < matrix[i][row]:
                    row = j
            for k in rows[i]:
                if matrix[i][row] == matrix[i][k]: ret.append(matrix[i][k])

        return ret
            
