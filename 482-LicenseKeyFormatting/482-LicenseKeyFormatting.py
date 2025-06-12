# Last updated: 12/6/2025, 5:49:04 am
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        val = ''
        for w in s:
            if w != '-': val += str(w).upper()
        
        ret = ""
        n = len(val)

        if n % k != 0:
            for i in range(n%k):
                ret += str(val[i])
            ret += '-'
        
        for i in range(n%k, (n-k)+1, k):
            for j in range(i, i+k):
                ret += str(val[j])
            ret += '-'
        
        return ret[:-1]