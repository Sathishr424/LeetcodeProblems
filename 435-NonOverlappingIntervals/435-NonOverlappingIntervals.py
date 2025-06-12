# Last updated: 12/6/2025, 5:49:29 am
class Solution:
    def eraseOverlapIntervals(self, inter: List[List[int]]) -> int:
        inter.sort(key=lambda x: x[0])
        curr = inter[0][1]
        ret = 0
        for i in range(1, len(inter)):
            if inter[i][0] >= curr:
                curr = inter[i][1]
            else:
                ret += 1
                if inter[i][1] < curr:
                    curr = inter[i][1]
        
        return ret
                
