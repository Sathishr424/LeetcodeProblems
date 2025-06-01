# Last updated: 1/6/2025, 7:40:08 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        start = cmax(0, n - (limit * 2))
        end = cmin(n, limit)

        ret = 0

        for i in range(start, end+1):
            rem = n - i
            s = cmax(0, rem - limit)
            e = cmin(rem, limit)

            ret += cmin(limit - s, e) + 1

        return ret