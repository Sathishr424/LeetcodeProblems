# Last updated: 2/10/2025, 4:19:02 am
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7

        m = r - l + 1
        dp = [[0, 0] for _ in range(m)]

        prefix = 0
        suffix = 0
        for i in range(m):
            if i + 1 < m:
                dp[i][1] = 1
            if i > 0:
                suffix += 1
                dp[i][0] = 1

        for i in range(n-1):
            next_suffix = 0
            for j in range(m):
                suffix = (suffix - dp[j][0]) % mod
                dp[j][0] = prefix
                next_suffix = (next_suffix + prefix) % mod

                prefix = (prefix + dp[j][1]) % mod
                dp[j][1] = suffix

            suffix = next_suffix
            prefix = 0

        ans = 0
        for i in range(m):
            ans += (dp[i][0] + dp[i][1]) % mod
            ans %= mod
        return ans