# Last updated: 10/27/2026, 2:12:15 PM
1class Solution:
2    def createGrid(self, m: int, n: int) -> list[str]:
3        ret = [['#'] * n for _ in range(m)]
4
5        for j in range(n):
6            ret[m-1][j] = '.'
7
8        for i in range(m):
9            ret[i][0] = '.'
10
11        return [''.join(row) for row in ret]