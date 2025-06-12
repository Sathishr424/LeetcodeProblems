# Last updated: 12/6/2025, 5:41:55 am
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        
        i = 1
        j = 0

        while i < n:
            if s[i] == s[j]:
                j += 1
                lps[i] = j
            elif j > 0:
                j = lps[j-1]
                continue
            i += 1
        
        return s[:lps[-1]]