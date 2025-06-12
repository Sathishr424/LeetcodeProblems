# Last updated: 12/6/2025, 5:54:49 am
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m > n: return -1
        
        lps = []
        i = 0
        lps.append(0)

        j = 1
        while j < m:
            if needle[i] == needle[j]: i += 1
            elif i > 0: 
                i = lps[i-1]
                continue
            lps.append(i)
            j += 1
        
        mtch = 0
        i = 0
        while i < n:
            if haystack[i] == needle[mtch]:
                mtch += 1
                if mtch == m: return i-m+1
            elif mtch > 0:
                mtch = lps[mtch-1]
                continue
            i += 1
        
        return -1
