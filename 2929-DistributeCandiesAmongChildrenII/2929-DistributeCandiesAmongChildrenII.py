# Last updated: 1/6/2025, 7:30:13 pm
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # if limit * 3 < n: return 0

        start = max(0, n - (limit * 2))
        end = limit
        ret = 0
        for i in range(start, end+1):
            rem = n - i
            s = max(0, rem - limit)
            e = min(rem, limit)

            diff = max(-1, min(limit - s, e)) + 1

            ret += diff
            # print(rem, (s, e), diff, ret)

        return ret

        