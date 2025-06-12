# Last updated: 12/6/2025, 5:37:03 am
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(1,n+1):
            for w in dictionary:
                if i-len(w) >= 0 and s[i-len(w):i] == w:
                    dp[i] = min(dp[i], dp[i-len(w)])
            dp[i] = min(dp[i], dp[i-1] + 1)
        return dp[-1]
        