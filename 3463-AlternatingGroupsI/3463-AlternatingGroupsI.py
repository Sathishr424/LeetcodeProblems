# Last updated: 12/6/2025, 5:35:34 am
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        alt = 1
        ret = 0

        for i in range(1, n+2):
            if alt == 3:
                ret += 1
                alt -= 1
            i = i % n
            if colors[i] != colors[i-1]:
                alt += 1
            else:
                alt = 1
        
        return ret+(alt==3)
        