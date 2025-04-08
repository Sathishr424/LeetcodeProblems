# Last updated: 9/4/2025, 2:55:48 am
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # matrix = [[1] * 200 for _ in range(200)]

        m = len(matrix)
        n = len(matrix[0])

        vis = [[0] * n for _ in range(m)]

        def dfs(i, j):
            matrix[i][j] = '0'
            if j+1 < n and matrix[i][j+1] == '1':
                vis[i][j] = dfs(i, j+1) + 1
            else:
                vis[i][j] = 1
            
            return vis[i][j]

        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    ret = max(ret, 1)
                    dfs(i, j)

        # for i in range(m):
        #     print(vis[i])
        
        for j in range(n):
            stack = []
            index = 0
            for i in range(m):
                curr = vis[i][j]
                index = i
                while stack and stack[-1][1] > curr:
                    index, val = stack.pop()
                    ret = max(ret, val * (i-index))
                stack.append((index, curr))
                # print(stack)
            i = m
            while stack:
                index, val = stack.pop()
                ret = max(ret, val * (i-index))

        # Edge cases
        # 1, 3, 3, 2, 3, 1, 3, 3, 3, 3, 3

        return ret