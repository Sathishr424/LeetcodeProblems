# Last updated: 13/4/2025, 9:25:46 pm
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