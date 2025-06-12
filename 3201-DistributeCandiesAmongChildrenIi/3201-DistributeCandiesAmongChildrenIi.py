# Last updated: 12/6/2025, 5:36:03 am
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        start = cmax(0, n - (limit * 2))
        end = cmin(n, limit)
        ret = 0

        for rem in range(n-start, n-end-1, -1):
            s = cmax(0, rem - limit)
            e = cmin(rem, limit)

            ret += cmin(limit - s, e) + 1

        return ret