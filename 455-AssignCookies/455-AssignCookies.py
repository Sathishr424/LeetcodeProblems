# Last updated: 13/7/2025, 11:39:12 am
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)

        s.sort()
        g.sort()

        l = 0
        r = 0
        ret = 0

        while l < n and r < m:
            if g[l] <= s[r]:
                ret += 1
                l += 1
                r += 1
            elif g[l] > s[r]:
                r += 1
        
        return ret
        