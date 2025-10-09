# Last updated: 9/10/2025, 9:14:18 pm
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                diff[r][c1] += 1
                diff[r][c2 + 1] -= 1

        mat = [[0] * n for _ in range(n)]
        curr = 0
        for i in range(n):
            for j in range(n):
                curr += diff[i][j]
                mat[i][j] = curr
            curr += diff[i][n]
        # [print(row) for row in mat]
        return mat