# Last updated: 25/4/2025, 1:36:40 am
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
        i = 0
        st = s[::-1]

        while i < n:
            if st[i] == s[j]:
                j += 1
            elif j > 0:
                j = lps[j-1]
                continue
            i += 1

        return s[j:][::-1] + s