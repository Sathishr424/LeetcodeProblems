# Last updated: 12/6/2025, 5:52:29 am
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        wordDict.sort(key=lambda x: len(x))
        for i in range(n):
            if i > 0 and not dp[i-1]: continue
            for w in wordDict:
                k = i+len(w)
                if k > n: break
                if s[i:k] == w: dp[k-1] = True
        return dp[-1]
