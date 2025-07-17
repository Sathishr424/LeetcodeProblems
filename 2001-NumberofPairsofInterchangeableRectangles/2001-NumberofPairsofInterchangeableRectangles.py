# Last updated: 17/7/2025, 8:28:40 pm
class Solution:
    def interchangeableRectangles(self, rect: List[List[int]]) -> int:
        n = len(rect)

        pair = defaultdict(int)
        ret = 0
        
        for i in range(n):
            curr = rect[i][0]/rect[i][1]

            ret += pair[curr]
            pair[curr] += 1
        
        return ret