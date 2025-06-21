# Last updated: 22/6/2025, 3:28:15 am
class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        n = len(coords)

        h = []
        v = []
        x = defaultdict(SortedList)
        y = defaultdict(SortedList)

        for x_, y_ in coords:
            x[x_].add(y_)
            y[y_].add(x_)
        
        h = sorted(x.keys())
        v = sorted(y.keys())
        # print(dict(x))
        # print(dict(y))
        ret = -1
        for x_ in h:
            if len(x[x_]) > 1:
                a = x[x_][0]
                b = x[x_][-1]

                base = abs(a-b)
                # print('X', x_, base, h[0], h[-1])
                if abs(x_ - h[0]) > 0:
                    ret = max(base * abs(x_ - h[0]), ret)
                if abs(x_ - h[-1]) > 0:
                    ret = max(ret, base * abs(x_ - h[-1]))
                # print((base, abs(x_ - h[0])), base * abs(x_ - h[0]), (base, abs(x_ - h[-1])), base * abs(x_ - h[-1]))
        
        for y_ in v:
            if len(y[y_]) > 1:
                a = y[y_][0]
                b = y[y_][-1]

                base = abs(a-b)
                # print('Y', y_, base, v[0], v[-1])
                if abs(y_ - v[0]) > 0:
                    ret = max(base * abs(y_ - v[0]), ret)
                if abs(y_ - v[-1]) > 0:
                    ret = max(ret, base * abs(y_ - v[-1]))
        
        return ret