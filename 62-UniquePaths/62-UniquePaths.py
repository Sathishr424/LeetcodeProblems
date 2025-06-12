# Last updated: 12/6/2025, 5:54:09 am
class Solution:
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        if m == 1 or n == 1: return 1
        if (m,n) in memo: return memo[(m,n)]
        elif (n,m) in memo: return memo[(n,m)]

        memo[(m,n)] = self.uniquePaths(m, n-1, memo) + self.uniquePaths(m-1, n, memo)
        return memo[(m,n)]