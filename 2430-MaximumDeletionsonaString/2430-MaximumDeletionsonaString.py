# Last updated: 24/9/2025, 11:28:34 pm
class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)

        half = n // 2
        dp = [[0] * n for _ in range(half + 1)]

        for window in range(1, half + 1):
            for i in range(window, n-window+1):
                curr = s[i:i+window]
                prev = s[i-window:i]
                if curr == prev:
                    dp[window][i-window] = 1

        @cache
        def rec(index):
            if index == n: return 0
            dis = n - index
            ans = 1
            for j in range(index, index + dis // 2):
                window = j - index + 1
                if dp[window][index]:
                    ans = max(ans, rec(j+1) + 1)

            return ans

        return rec(0)
                