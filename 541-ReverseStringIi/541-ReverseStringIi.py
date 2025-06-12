# Last updated: 12/6/2025, 5:48:34 am
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        if n <= k: return s[::-1]
        ret = ""
        for i in range(0, n, k*2):
            for j in range(min(n-1, i+k-1), i-1, -1):
                ret += s[j]
            for j in range(i+k, min(n, i+(k*2))):
                ret += s[j]
        
        return ret