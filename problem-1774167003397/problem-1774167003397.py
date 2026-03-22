# Last updated: 3/22/2026, 1:40:03 PM
1class Solution:
2    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
3        n = len(mat)
4        def rotate(mat, retry):
5            rotated = [[0] * n for _ in range(n)]
6            for i in range(n):
7                for j in range(n):
8                    rotated[i][j] = mat[n-j-1][i]
9            
10            for i in range(n):
11                for j in range(n):
12                    if rotated[i][j] != target[i][j]:
13                        if retry < 3: return rotate(rotated, retry + 1)
14                        return False
15            return True
16
17        return rotate(mat, 0)