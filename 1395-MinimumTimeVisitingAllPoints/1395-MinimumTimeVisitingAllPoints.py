# Last updated: 12/6/2025, 5:42:40 am
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        p_x, p_y = points[0]
        ret = 0
        for i in range(1, len(points)):
            x, y = points[i]
            if x == p_x:
                ret += abs(p_y - y)
            elif y == p_y:
                ret += abs(p_x - x)
            else:
                diff_x = abs(p_x - x)
                diff_y = abs(p_y - y)
                if diff_x > diff_y:
                    ret += diff_y + abs(diff_x - diff_y)
                else:
                    ret += diff_x + abs(diff_x - diff_y)
            p_x, p_y = x, y
        return ret

