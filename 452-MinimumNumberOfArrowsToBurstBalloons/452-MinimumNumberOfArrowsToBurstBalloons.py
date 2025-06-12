# Last updated: 12/6/2025, 5:49:16 am
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev = points[0][1]
        ret = 1
        for i in range(1, len(points)):
            if points[i][0] <= prev:
                prev = min(points[i][1], prev)
            else:
                prev = points[i][1]
                ret += 1
        return ret