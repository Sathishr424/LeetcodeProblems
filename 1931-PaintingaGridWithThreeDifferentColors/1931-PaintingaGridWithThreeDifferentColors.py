# Last updated: 16/5/2025, 6:15:53 am
mod = 10**9 + 7

def matrixMulti(matrix_1, matrix_2):
    m = len(matrix_1)
    n = len(matrix_2[0])
    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
                result[i][j] %= mod
    return result

def matrixPow(matrix, power):
    if power == 1: return matrix
    
    ans = matrixPow(matrix, power // 2)
    ans = matrixMulti(ans, ans)
    if power % 2:
        ans = matrixMulti(ans, matrix)
    return ans

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        size = 0
        relation = {}

        def findNeighbors(full_comb, comb, index, neighbor, prev):
            if index == 0:
                matrix[relation[full_comb]][relation[neighbor]] = 1
                return
            
            rem = comb % 3
            for color in range(3):
                if color == rem or color == prev: continue
                findNeighbors(full_comb, comb // 3, index-1, neighbor * 3 + color, color)

        combs = []

        def generate(comb, index):
            nonlocal size
            if index == m:
                relation[comb] = size
                size += 1
                combs.append(comb)
                return
            
            prev = comb % 3
            for color in range(3):
                if color == prev and index > 0: continue
                generate(comb * 3 + color, index+1)
        
        generate(0, 0)
        if n == 1: return len(combs)
        
        matrix = [[0] * size for _ in range(size)]
        for comb in combs:
            findNeighbors(comb, comb, m, 0, -1)

        if n > 1:
            matrix = matrixPow(matrix, n-1)

        curr = [[1] * len(combs)]
        ret = matrixMulti(curr, matrix)
        return sum(ret[0]) % mod
            
