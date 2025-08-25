# Last updated: 25/8/2025, 2:40:43 pm
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        traverse = []

        for i in range(n):
            traverse.append((0, i))
        
        for i in range(1, m):
            traverse.append((i, n-1))
        
        def backward(i, j, arr):
            if i == m or j < 0: return
            backward(i+1, j-1, arr)
            arr.append(mat[i][j])
        
        def forward(i, j, arr):
            if i == m or j < 0: return
            arr.append(mat[i][j])
            forward(i+1, j-1, arr)

        is_rev = True
        ret = []
        for i, j in traverse:
            if is_rev:
                backward(i, j, ret)
            else:
                forward(i, j, ret)
            is_rev = not is_rev

        return ret
