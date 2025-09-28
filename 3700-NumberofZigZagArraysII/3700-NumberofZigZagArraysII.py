# Last updated: 28/9/2025, 8:32:18 pm
mod = 10**9 + 7

def multiplyMatrix(x, y):
    m = len(x)
    ret = [[0] * m for _ in range(m)]
    
    for row in range(m):
        for j in range(m):
            curr = 0
            for i in range(m):
                curr += x[row][i] * y[i][j] % mod
            ret[row][j] = curr % mod
    
    return ret

def matrixPow(matrix, power):
    if power == 1: return matrix

    half = power // 2

    ans = matrixPow(matrix, half)
    ans = multiplyMatrix(ans, ans)
    if power % 2:
        ans = multiplyMatrix(ans, matrix)
    
    return ans

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        m2 = 2 * m
        matrix = [[0] * m2 for _ in range(m2)]

        for i in range(m):
            if i > 0:
                for j in range(i):
                    matrix[m + i][j] = 1
            
            if i + 1 < m:
                for j in range(i+1, m):
                    matrix[i][m + j] = 1
    
        # [print(row) for row in matrix]

        matrix = matrixPow(matrix, n - 1)
        # print()
        # [print(row) for row in matrix]
        ans = 0
        for i in range(m2):
            for j in range(m2):
                ans = (ans + matrix[i][j]) % mod
        
        return ans % mod