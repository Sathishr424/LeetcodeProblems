# Last updated: 31/5/2025, 10:09:37 pm
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(l, r):
            if l == r: return 1
            elif l > r: return 0

            if s[l] == s[r]:
                return dfs(l+1, r-1) + 2
            return max(dfs(l+1, r), dfs(l, r-1))
        
        return dfs(0, len(s)-1)