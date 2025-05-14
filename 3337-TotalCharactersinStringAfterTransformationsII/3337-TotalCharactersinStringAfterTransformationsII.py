# Last updated: 14/5/2025, 10:02:25 pm
mod = 10**9 + 7

def matrix_multiplication(matrix_x, matrix_y):
    new_matrix = [[0] * 26 for _ in range(26)]
    for i in range(26):
        for j in range(26):
            curr = 0
            for k in range(26):
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
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        matrix = [[0] * 26 for _ in range(26)]

        for i in range(26):
            for j in range(nums[i]):
                matrix[(i+j+1) % 26][i] = 1

        matrix = matrix_pow(matrix, t)

        freq = [0] * 26
        for char in s:
            freq[ord(char) - 97] += 1

        ans = 0
        for j in range(26):
            curr = 0
            for k in range(26):
                curr = (curr + freq[k] * matrix[j][k] % mod) % mod
            ans = (ans + curr) % mod
     
        return ans