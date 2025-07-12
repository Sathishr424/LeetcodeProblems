# Last updated: 12/7/2025, 2:13:45 pm
inf = float('inf')
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer -= 1
        secondPlayer -= 1
        max_round = floor(log2(n)) + 1

        @cache
        def rec(mask, l, r, rnd):
            while l <= r and mask & (1 << l) != 0:
                l += 1
            
            while r >= l and mask & (1 << r) != 0:
                r -= 1

            if l < r:
                if l == firstPlayer and r == secondPlayer:
                    return rnd + 1, rnd + 1
                elif l == firstPlayer:
                    return rec(mask | (1 << r), l + 1, r - 1, rnd)
                elif r == secondPlayer:
                    return rec(mask | (1 << l), l + 1, r - 1, rnd)
                l1, r1 = rec(mask | (1 << l), l + 1, r - 1, rnd)
                l2, r2 = rec(mask | (1 << r), l + 1, r - 1, rnd)
                return cmin(l1, l2), cmax(r1, r2)
            else:
                if rnd + 1 > max_round: return inf, -1
                return rec(mask, 0, n-1, rnd + 1)

        left, right = rec(0, 0, n-1, 0)

        rec.cache_clear()
        # print(left, right)
        return [left, right]