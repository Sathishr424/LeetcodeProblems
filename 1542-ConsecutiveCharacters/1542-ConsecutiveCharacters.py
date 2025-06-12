# Last updated: 12/6/2025, 5:41:46 am
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        ret = 1; maxSS = 1;
        for i in range(1,len(s)):
            if s[i] == s[i-1]: ret += 1
            elif ret > maxSS: 
                maxSS = ret
                ret = 1
            else: ret = 1
        if ret > maxSS: maxSS = ret
        return maxSS