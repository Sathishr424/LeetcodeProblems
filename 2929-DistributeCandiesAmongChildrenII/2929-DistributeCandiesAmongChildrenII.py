# Last updated: 10/8/2025, 6:41:34 am
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ret = 0
        for i in range(min(n, limit) + 1):
            rem = n - i

            if rem - limit > limit: continue

            can = max(0, rem - limit)

            ret += rem - can * 2 + 1
        
        return ret