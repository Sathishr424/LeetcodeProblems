# Last updated: 12/6/2025, 5:49:15 am
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        n = len(g)
        m = len(s)

        i = 0
        j = 0
        while i < n and j < m:
            if s[j] >= g[i]: i += 1
            j += 1
        
        return i