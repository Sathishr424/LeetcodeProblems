# Last updated: 12/6/2025, 5:40:55 am
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    rows[i] += 1
                    cols[j] += 1
        ret = 0       
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if rows[i] == n-1 and cols[j] == m-1: ret += 1
        
        return ret