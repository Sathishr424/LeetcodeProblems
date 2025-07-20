# Last updated: 20/7/2025, 10:01:11 am
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