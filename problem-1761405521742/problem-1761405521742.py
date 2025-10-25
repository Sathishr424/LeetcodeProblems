# Last updated: 25/10/2025, 8:48:41 pm
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        maxi = max( [max(mat[i]) for i in range(m)] ) + 1
        
        mod = 10**9 + 7
        dp = [[-1] * maxi for _ in range(m)]

        def rec(i, g):
            if i == m:
                return 1 if g == 1 else 0
            if dp[i][g] != -1: return dp[i][g]

            ans = 0
            for j in range(n):
                ans += rec(i + 1, gcd(g, mat[i][j]))

            dp[i][g] = ans % mod
            return dp[i][g]

        return rec(0, 0)