# Last updated: 12/6/2025, 5:46:19 am
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        prev = float('inf')
        index = -1
        ret = [0] * n
        
        def rec(i):
            if i == n: return index
            elif s[i] == c: return i
            ind = rec(i+1)
            ret[i] = min(abs(i-prev), abs(i-ind))
            return ind
        
        j = 0

        while j < n:
            if j > index:
                prev = index if index >= 0 else float('inf')
                index = rec(j)
                j = max(j, index)
            ret[j] = min(abs(j-prev), abs(j-index))
            j += 1
        
        return ret

