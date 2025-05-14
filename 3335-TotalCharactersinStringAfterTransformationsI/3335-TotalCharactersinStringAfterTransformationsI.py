# Last updated: 14/5/2025, 5:04:10 pm
N = 10**5 + 1
mod = 10**9 + 7

dp = [[1] * 26] + [[0] * 26 for i in range(N-1)]

for i in range(1, N):
    for j in range(25):
        dp[i][j] = (dp[i][j] + dp[i-1][j + 1]) % mod
    dp[i][25] = (dp[i][25] + dp[i-1][0] + dp[i-1][1]) % mod

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        ret = 0
        for char in s:
            ret = (ret + dp[t][ord(char) - 97]) % mod

        return ret