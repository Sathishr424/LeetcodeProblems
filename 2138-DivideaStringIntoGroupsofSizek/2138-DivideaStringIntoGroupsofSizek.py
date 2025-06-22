# Last updated: 22/6/2025, 5:36:12 am
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        curr = ''
        ret = []
        for i in range(n):
            curr += s[i]
            if len(curr) == k:
                ret.append(curr)
                curr = ''
        
        if curr:
            ret.append( curr + ( fill * (k - len(curr)) ) )
        return ret