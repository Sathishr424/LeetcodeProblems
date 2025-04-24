# Last updated: 25/4/2025, 1:40:29 am
class Solution:
    def shortestPalindrome(self, s: str) -> str:
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
        
        j = 0
        i = n-1

        while i >= 0:
            if s[i] == s[j]:
                j += 1
            elif j > 0:
                j = lps[j-1]
                continue
            i -= 1

        return s[j:][::-1] + s