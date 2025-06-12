# Last updated: 12/6/2025, 5:43:48 am
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = {}
        for t in tiles:
            if t in counts:
                counts[t] += 1
            else:
                counts[t] = 1

        n = len(tiles)
        ret = {}
        def rec(st):
            if len(st) == n: return

            for t in tiles:
                if counts[t] > 0:
                    counts[t] -= 1
                    tmp = st + t
                    ret[tmp] = 1
                    rec(tmp)
                    counts[t] += 1
        
        rec('')
        return len(ret)