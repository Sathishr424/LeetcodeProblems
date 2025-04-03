# Last updated: 3/4/2025, 10:26:42 pm
cmax = lambda x, y: x if x > y else y

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)

        if m < n: return 0

        def possible(t):
            needed = 0
            add = 0
            prev = -1

            for p in points:
                sub = cmax(0, ceil(t / p) - add)
                x = cmax(0, sub * 2 - 1)

                needed += x
                if prev == 0: needed += 1
                prev = x
                add = cmax(0, sub-1)

                if needed > m: return False
            return needed <= m
        
        l = 1
        r = 10**15
        ans = 0

        while l <= r:
            mid = (l+r) // 2
            if possible(mid):
                l = mid+1
                ans = cmax(ans, mid)
            else:
                r = mid-1
            
        return ans
