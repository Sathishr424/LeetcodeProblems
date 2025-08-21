# Last updated: 21/8/2025, 5:12:30 pm
cmax = lambda x, y: x if x > y else y

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        v = [[0] * n for _ in range(m)]

        for j in range(n):
            for i in range(m):
                if matrix[i][j] == '1':
                    v[i][j] = v[i - 1][j] + 1
        
        max_rect = 0
        stack = []
        for i in range(m):
            for j in range(n):
                left = j
                while stack and stack[-1][0] > v[i][j]:
                    height, left = stack.pop()
                    max_rect = cmax(max_rect, height * (j - left))
                stack.append((v[i][j], left))

            right = n
            while stack:
                height, left = stack.pop()
                max_rect = cmax(max_rect, height * (right - left))

        return max_rect