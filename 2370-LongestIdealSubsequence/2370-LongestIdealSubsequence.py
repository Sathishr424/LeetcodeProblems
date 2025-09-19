# Last updated: 20/9/2025, 12:56:57 am
cmax = lambda x, y: x if x > y else y

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        alp = [ord(char) - ord('a') for char in s]

        dp = [[0] * 26 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            a = alp[i - 1]
            for j in range(max(0, a - k), min(26, a + k + 1)):
                dp[i][j] = cmax(dp[i - 1][a] + 1, dp[i - 1][j])

            for j in range(26):
                dp[i][j] = cmax(dp[i][j], dp[i - 1][j])

        return max(dp[-1])