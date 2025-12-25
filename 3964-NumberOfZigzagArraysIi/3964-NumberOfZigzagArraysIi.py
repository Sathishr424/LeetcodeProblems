# Last updated: 12/25/2025, 7:09:49 PM
mod = 10**9 + 7

def multiplyMatrix(x, y):
    m = len(x)
    n = len(y[0])
    ret = [[0] * n for _ in range(m)]
    
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
            for j in range(i):
                matrix[m + i][j] = 1
            
            for j in range(i+1, m):
                matrix[i][m + j] = 1

        matrix = matrixPow(matrix, n + 1)
        
        if n % 2:
            return (matrix[0][0] + matrix[-1][-1]) % mod
        else:
            return (matrix[0][-1] + matrix[-1][0]) % mod