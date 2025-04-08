# Last updated: 9/4/2025, 3:02:39 am
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        vis = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    vis[i][j] = vis[i][j+1] + 1 if j+1 < n else 1
        
        stack = []
        ret = 0
        for j in range(n):
            for i in range(m):
                index = i
                while stack and stack[-1][1] > vis[i][j]:
                    index, val = stack.pop()
                    ret = max(ret, val * (i-index))
                stack.append((index, vis[i][j]))

            i = m
            while stack:
                index, val = stack.pop()
                ret = max(ret, val * (i-index))

        # 1, 3, 3, 2, 3, 1, 3, 3, 3, 3, 3
        return ret