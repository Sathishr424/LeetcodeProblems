# Last updated: 12/6/2025, 5:54:02 am
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        
        l = 1
        r = x // 2 + 1

        while l < r:
            mid = (l + r) // 2

            if mid * mid > x:
                r = mid
            else:
                l = mid + 1
        
        return l-1