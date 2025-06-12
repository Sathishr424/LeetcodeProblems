# Last updated: 12/6/2025, 5:34:19 am
class Solution:
    def countArrays(self, orig: List[int], bounds: List[List[int]]) -> int:
        n = len(bounds)
        for i in range(1, n):
            need = orig[i] - orig[i-1]
            prev = bounds[i-1]
            curr = bounds[i]

            # (2, 7), (5, 13) => (4, 7), (5, 8)
            # (5, 10), (2, 10) => (5, 9), (6, 10)

            x = curr[0] - prev[0] - need
            y = curr[1] - prev[1] - need

            if x > 0:
                prev[0] += x
            else:
                curr[0] -= x
            
            if y > 0:
                curr[1] -= y
            else:
                prev[1] += y

            can = curr[1] - curr[0] + 1
            if can <= 0: return 0
        
        return can