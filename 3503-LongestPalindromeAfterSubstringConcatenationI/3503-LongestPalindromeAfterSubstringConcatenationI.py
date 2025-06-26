# Last updated: 27/6/2025, 2:23:48 am
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ret = []

        def rec(curr, index, st):
            if len(curr) and curr == curr[::-1]:
                rec('', index, st + [curr])
            
            if index == n:
                if len(curr) == 0:
                    ret.append(st)
                return
            
            rec(curr + s[index], index+1, st)
        
        rec('', 0, [])
        return ret
