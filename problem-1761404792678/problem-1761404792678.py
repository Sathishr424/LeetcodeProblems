# Last updated: 25/10/2025, 8:36:32 pm
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        mod = 10**9 + 7

        @cache
        def rec(i, g):
            if i == m:
                return 1 if g == 1 else 0

            ans = 0
            for j in range(n):
                ans += rec(i + 1, gcd(g, mat[i][j]))

            return ans % mod

        ans = rec(0, 0)
        rec.cache_clear()
        return ans