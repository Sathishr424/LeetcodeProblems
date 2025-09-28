# Last updated: 28/9/2025, 9:21:37 pm
def multiplyMatrix(x, y):
    m = len(x)
    n = len(y[0])
    ret = [[0] * n for _ in range(m)]
    
    for row in range(m):
        for j in range(m):
            curr = 0
            for i in range(m):
                curr += x[row][i] * y[i][j]
            ret[row][j] = curr
    
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
    def fib(self, n: int) -> int:
        if n <= 1: return n

        matrix = [[1, 1], [1, 0]]

        matrix = matrixPow(matrix, n-1)

        # [print(row) for row in matrix]

        return matrix[0][0]