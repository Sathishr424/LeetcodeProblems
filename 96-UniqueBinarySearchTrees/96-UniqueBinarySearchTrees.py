# Last updated: 5/8/2025, 11:24:29 am
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        if m < n:
            m, n = n, m
            str1, str2 = str2, str1
        
        d = gcd(m, n)
        ret = str2[:d]

        for i in range(0, m, d):
            if str1[i:i+d] != ret: return ''
        
        for i in range(0, n, d):
            if str2[i:i+d] != ret: return ''
        
        return ret