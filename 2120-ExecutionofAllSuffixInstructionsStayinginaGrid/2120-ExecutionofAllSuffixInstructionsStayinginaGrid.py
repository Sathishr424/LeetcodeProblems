# Last updated: 20/6/2025, 9:50:49 am
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        def rec(index, i, j):
            if index == m: return 0
            if s[index] == 'L':
                if j-1 < 0: return 0
                return rec(index+1, i, j-1) + 1
            elif s[index] == 'R':
                if j+1 == n: return 0
                return rec(index+1, i, j+1) + 1
            elif s[index] == 'U':
                if i-1 < 0: return 0
                return rec(index+1, i-1, j) + 1
            elif s[index] == 'D':
                if i+1 == n: return 0
                return rec(index+1, i+1, j) + 1
        ret = []
        for i in range(m):
            ret.append(rec(i, *startPos))
        
        return ret