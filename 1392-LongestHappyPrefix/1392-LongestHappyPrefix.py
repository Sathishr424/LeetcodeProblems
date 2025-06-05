# Last updated: 5/6/2025, 6:05:48 pm
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