# Last updated: 12/6/2025, 5:48:25 am
N = 10**5
mod = 10**9 + 7
dp = [[[0] * 2 for _ in range(3)] for _ in range(N)]

dp[0][0][0] = 1
dp[0][0][1] = 1

dp[0][1][0] = 1
dp[0][1][1] = 0

dp[0][2][0] = 0
dp[0][2][1] = 0

# l = 0, a = 0 => (0, a), (l+1, a) (0, a+1)
# l = 1, a = 0 => (0, a), (l+1, a) (0, a+1)
# l = 2, a = 0 => (0, a), (0, a+1)

# l = 0, a = 1 => (0, a), (l+1, a)
# l = 1, a = 1 => (0, a), (l+1, a)
# l = 2, a = 1 => (0, a)

for i in range(N-1):
    for l in range(3):
        for a in range(2):
            dp[i+1][0][a] = (dp[i+1][0][a] + dp[i][l][a]) % mod

            if l < 2:
                dp[i+1][l+1][a] = (dp[i+1][l+1][a] + dp[i][l][a]) % mod
            
            if a == 0:
                dp[i+1][0][a+1] = (dp[i+1][0][a+1] + dp[i][l][a]) % mod

class Solution:
    def checkRecord(self, n: int) -> int:
        ret = 0
        n -= 1
        for i in range(3):
            for j in range(2):
                ret = (ret + dp[n][i][j]) % mod
        return ret