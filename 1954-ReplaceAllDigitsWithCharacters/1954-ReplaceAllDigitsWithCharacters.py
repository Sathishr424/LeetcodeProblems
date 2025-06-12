# Last updated: 12/6/2025, 5:39:46 am
class Solution:
    def replaceDigits(self, s: str) -> str:
        alp = list("abcdefghijklmnopqrstuvwxyz")
        ret = ""
        for i in range(len(s)):
            if s[i].isdigit(): ret += alp[alp.index(s[i-1])+int(s[i])]
            else:  ret += s[i]
        return ret