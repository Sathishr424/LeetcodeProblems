# Last updated: 1/13/2026, 12:40:21 AM
1class Solution:
2    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
3        p_x, p_y = points[0]
4        ret = 0
5        for i in range(1, len(points)):
6            x, y = points[i]
7            if x == p_x:
8                ret += abs(p_y - y)
9            elif y == p_y:
10                ret += abs(p_x - x)
11            else:
12                diff_x = abs(p_x - x)
13                diff_y = abs(p_y - y)
14                if diff_x > diff_y:
15                    ret += diff_y + abs(diff_x - diff_y)
16                else:
17                    ret += diff_x + abs(diff_x - diff_y)
18            p_x, p_y = x, y
19        return ret
20