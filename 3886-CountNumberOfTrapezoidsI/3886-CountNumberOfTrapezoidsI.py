# Last updated: 12/25/2025, 7:11:12 PM
mod = 10**9 + 7

@cache
def fact(x):
    return factorial(x)

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)

        hor = defaultdict(int)

        for x, y in points:
            hor[y] += 1

        if len(hor) == 1: return 0
        ret = 0
        prev = 0
        # print(hor)
        for h in hor:
            cnt = hor[h]
            if cnt == 1: continue
            curr = cnt * (cnt - 1) // 2
            ret += prev * curr % mod
            ret %= mod
            prev += curr
            prev %= mod

        return ret