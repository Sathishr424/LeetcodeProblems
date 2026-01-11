# Last updated: 1/11/2026, 10:54:02 PM
1cmax = lambda x, y: x if x > y else y
2
3class Solution:
4    def maximalRectangle(self, matrix: List[List[str]]) -> int:
5        m = len(matrix)
6        n = len(matrix[0])
7
8        v = [[0] * n for _ in range(m)]
9
10        for j in range(n):
11            for i in range(m):
12                if matrix[i][j] == '1':
13                    v[i][j] = v[i - 1][j] + 1
14        
15        max_rect = 0
16        stack = []
17        for i in range(m):
18            for j in range(n):
19                left = j
20                while stack and stack[-1][0] > v[i][j]:
21                    height, left = stack.pop()
22                    max_rect = cmax(max_rect, height * (j - left))
23                stack.append((v[i][j], left))
24
25            right = n
26            while stack:
27                height, left = stack.pop()
28                max_rect = cmax(max_rect, height * (right - left))
29
30        return max_rect