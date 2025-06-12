# Last updated: 12/6/2025, 5:45:02 am
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        ret = []
        curr = n
        for i in range(n):
            if s[i] == 'I':
                ret.append(curr-(n-i))
            else:
                ret.append(curr)
                curr -= 1
        
        ret.append(curr)
        return ret

        


