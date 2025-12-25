# Last updated: 12/25/2025, 7:11:22 PM
inf = float('inf')
cmax = lambda x, y: x if x > y else y
cmin = lambda x, y: x if x < y else y
class Node:
    def __init__(self):
        self.min = inf
        self.max = 0
        self.cnt = 0
class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        n = len(coords)

        h = []
        v = []
        x = defaultdict(Node)
        y = defaultdict(Node)

        for x_, y_ in coords:
            x[x_].min = cmin(x[x_].min, y_)
            x[x_].max = cmax(x[x_].max, y_)
            x[x_].cnt += 1

            y[y_].min = cmin(y[y_].min, x_)
            y[y_].max = cmax(y[y_].max, x_)
            y[y_].cnt += 1
        
        h = sorted(x.keys())
        v = sorted(y.keys())

        ret = -1
        for x_ in h:
            if x[x_].cnt == 1: continue
            a = x[x_].min
            b = x[x_].max

            base = b-a
            if x_ - h[0] > 0:
                ret = cmax(base * (x_ - h[0]), ret)
            if h[-1] - x_ > 0:
                ret = cmax(ret, base * (h[-1] - x_))

        for y_ in v:
            if y[y_].cnt == 1: continue
            a = y[y_].min
            b = y[y_].max

            base = b-a
            if y_ - v[0] > 0:
                ret = cmax(base * (y_ - v[0]), ret)
            if v[-1] - y_ > 0:
                ret = cmax(ret, base * (v[-1] - y_))
        
        return ret