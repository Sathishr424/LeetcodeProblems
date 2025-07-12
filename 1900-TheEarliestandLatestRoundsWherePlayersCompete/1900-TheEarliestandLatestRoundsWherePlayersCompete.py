# Last updated: 12/7/2025, 2:10:46 pm
inf = float('inf')
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer -= 1
        secondPlayer -= 1
        max_round = floor(log2(n)) + 1

        @cache
        def rec_earliest(mask, l, r, rnd):
            # print(format(mask, f'0{n}b'), l, r, rnd)
            while l <= r and mask & (1 << l) != 0:
                l += 1
            
            while r >= l and mask & (1 << r) != 0:
                r -= 1

            if l < r:
                if l == firstPlayer and r == secondPlayer:
                    return rnd + 1
                if l == firstPlayer:
                    return rec_earliest(mask | (1 << r), l + 1, r - 1, rnd)
                elif r == secondPlayer:
                    return rec_earliest(mask | (1 << l), l + 1, r - 1, rnd)
                    
                return min(rec_earliest(mask | (1 << l), l + 1, r - 1, rnd), rec_earliest(mask | (1 << r), l + 1, r - 1, rnd))
            else:
                if rnd + 1 > max_round: return inf
                return rec_earliest(mask, 0, n-1, rnd + 1)
        
        @cache
        def rec_latest(mask, l, r, rnd):
            # print(format(mask, f'0{n}b'), l, r, rnd)
            while l <= r and mask & (1 << l) != 0:
                l += 1
            
            while r >= l and mask & (1 << r) != 0:
                r -= 1

            if l < r:
                if l == firstPlayer and r == secondPlayer:
                    return rnd + 1
                if l == firstPlayer:
                    return rec_latest(mask | (1 << r), l + 1, r - 1, rnd)
                elif r == secondPlayer:
                    return rec_latest(mask | (1 << l), l + 1, r - 1, rnd)
                    
                return max(rec_latest(mask | (1 << l), l + 1, r - 1, rnd), rec_latest(mask | (1 << r), l + 1, r - 1, rnd))
            else:
                if rnd + 1 > max_round: return -1
                return rec_latest(mask, 0, n-1, rnd + 1)
        

        left = rec_earliest(0, 0, n-1, 0)
        right = rec_latest(0, 0, n-1, 0)

        rec_earliest.cache_clear()
        rec_latest.cache_clear()
        # print(left, right)
        return [left, right]