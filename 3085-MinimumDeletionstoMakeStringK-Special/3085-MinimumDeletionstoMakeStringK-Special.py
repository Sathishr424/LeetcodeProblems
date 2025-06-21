# Last updated: 21/6/2025, 10:27:07 am
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for char in word:
            freq[ord(char) - 97] += 1

        arr = sorted([freq[i] for i in range(26) if freq[i]])
        n = len(arr)
        dp = [[float('inf')] * n for _ in range(n)]
        # for i in range(n):
        #     dp[i][n-1] = 0
        dp[0][n-1] = 0
        # print(arr)

        ret = float('inf')
        for i in range(n):
            s = 0
            for j in range(n-1, i, -1):
                diff = arr[j] - arr[i]
                if diff > k:
                    dp[i+1][j] = min(dp[i+1][j], arr[i] + dp[i][j])
                    dp[i][j-1] = min(diff - k + dp[i][j], dp[i][j-1])
                else:
                    dp[i+1][j] = dp[i][j]
                    dp[i][j-1] = dp[i][j]

            ret = min(ret, dp[i][i])

        return ret