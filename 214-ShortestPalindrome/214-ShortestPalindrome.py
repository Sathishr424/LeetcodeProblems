# Last updated: 25/4/2025, 1:35:33 am
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)

        def kmp(st):
            m = len(st)
            lps = [0] * m
            i = 1
            j = 0

            while i < m:
                if st[i] == st[j]:
                    j += 1
                    lps[i] = j
                elif j > 0:
                    j = lps[j-1]
                    continue
                i += 1
            return lps
        
        x = kmp(s)
        j = 0
        i = 0
        st = s[::-1]
        
        while i < n:
            if st[i] == s[j]:
                j += 1
            elif j > 0:
                j = x[j-1]
                continue
            i += 1

        return s[j:][::-1] + s