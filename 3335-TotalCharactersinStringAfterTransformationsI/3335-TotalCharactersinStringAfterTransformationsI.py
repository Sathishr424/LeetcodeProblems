# Last updated: 14/5/2025, 10:36:11 pm
mod = 10**9 + 7

def matrix_multiplication(matrix_x, matrix_y):
    m = len(matrix_x)
    n = len(matrix_y[0])
    new_matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            curr = 0
            for k in range(n):
                curr = (curr + matrix_x[i][k] * matrix_y[k][j] % mod) % mod
            new_matrix[i][j] = curr
    return new_matrix

def matrix_pow(matrix, power):
    if power == 1: return matrix
    ans = matrix_pow(matrix, power // 2)
    ans = matrix_multiplication(ans, ans)
    if power % 2:
        ans = matrix_multiplication(ans, matrix)
    return ans

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        matrix = [[0] * 26 for _ in range(26)]

        for i in range(25):
            matrix[i][i+1] = 1
        
        matrix[25][0] = 1
        matrix[25][1] = 1

        matrix = matrix_pow(matrix, t)

        freq = [[0] * 26]
        for char in s:
            freq[0][ord(char) - 97] += 1

        return sum(matrix_multiplication(freq, matrix)[0]) % mod