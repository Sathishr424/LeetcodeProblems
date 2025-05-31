# Last updated: 31/5/2025, 11:57:15 pm
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        dp = [[[-1] * (k+1) for _ in range(n)] for _ in range(n)]

        def dfs(l, r, k):
            if dp[l][r][k] != -1: return dp[l][r][k]
            if l == r: return 1
            elif l > r: return 0

            ans = max(dfs(l+1, r, k), dfs(l, r-1, k))

            diff = abs(ord(s[l]) - ord(s[r]))
            diff = min(26 - diff, diff)

            if diff <= k:
                ans = max(ans, dfs(l+1, r-1, k-diff) + 2)
            dp[l][r][k] = ans
            return ans
        
        return dfs(0, len(s)-1, k)