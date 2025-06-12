# Last updated: 12/6/2025, 5:48:19 am
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c: return mat
        ret = []
        for i in range(r):
            ret.append([0] * c)
        
        for pos in range(r*c):
            ret[pos//c][pos%c] = mat[pos//n][pos % n]
        
        return ret