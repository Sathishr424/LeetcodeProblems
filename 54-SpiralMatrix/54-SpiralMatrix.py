# Last updated: 12/6/2025, 5:54:23 am
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        rows = [0] * m
        cols = [0] * n
        def goRight(i, left, right):
            while left <= right and cols[left] == 0:
                ret.append(matrix[i][left])
                left += 1
            rows[i] = 1
            if i+1 < m and rows[i+1] == 0: return goDown(left-1, i+1, m-1)
        def goDown(j, top, bottom):
            while top <= bottom and rows[top] == 0:
                ret.append(matrix[top][j])
                top += 1
            cols[j] = 1
            if j-1 >= 0 and cols[j-1] == 0: return goLeft(top-1, 0, j-1)
        def goLeft(i, left, right):
            while right >= left and cols[right] == 0:
                ret.append(matrix[i][right])
                right -= 1
            rows[i] = 1
            if i-1 >= 0 and rows[i-1] == 0: return goUp(right+1, 0, i-1)
        def goUp(j, top, bottom):
            while bottom >= top and rows[bottom] == 0:
                ret.append(matrix[bottom][j])
                bottom -= 1
            cols[j] = 1
            if j+1 < n and cols[j+1] == 0: return goRight(bottom+1, j+1, n-1)
        goRight(0, 0, n-1)
        return ret