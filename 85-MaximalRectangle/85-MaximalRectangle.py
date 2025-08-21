# Last updated: 21/8/2025, 3:33:47 pm
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        h = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    h[i][j] = h[i][j + 1] + 1
        
        # [print(row) for row in h]

        max_ret = 0
        for j in range(n):
            stack = deque([])
            for i in range(m):
                cnt = 0
                while stack and stack[-1][0] >= h[i][j]:
                    v, c = stack.pop()
                    cnt += c + 1
                    max_ret = max(max_ret, v * cnt)
                stack.append((h[i][j], cnt))
                # print(j, stack)
            tot_cnt = 0
            for _, c in stack:
                tot_cnt += c + 1
            while stack:
                v, c = stack.popleft()
                # print(stack, tot_cnt, (v, c))
                max_ret = max(max_ret, v * tot_cnt)
                tot_cnt -= c + 1

        return max_ret