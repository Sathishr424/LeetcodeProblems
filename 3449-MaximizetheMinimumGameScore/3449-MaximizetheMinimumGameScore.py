# Last updated: 3/4/2025, 10:22:41 pm
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)

        if m < n: return 0

        def possible(t):
            needed = 0
            add = 0
            skipAdd = 0
            for p in points:
                sub = ceil(t / p)

                if add >= sub:
                    add = 0
                    skipAdd += 1
                else:
                    sub -= add
                    x = sub * 2 - 1
                    needed += x + skipAdd
                    
                    add = max(0, sub-1)
                    skipAdd = 0
                    if needed > m: return False
            return needed <= m
        
        l = 1
        r = 10**16
        ans = 0

        while l <= r:
            mid = (l+r) // 2
            if possible(mid):
                l = mid+1
                ans = max(ans, mid)
            else:
                r = mid-1
            
        return ans
