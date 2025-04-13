# Last updated: 13/4/2025, 9:20:33 pm
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        elif x == 1: return 1
        l = 1
        r = x // 2 + 1

        while l < r:
            mid = (l + r) // 2
            val = mid * mid

            if val >= x:
                r = mid
            else:
                l = mid + 1
        
        return l if l*l == x else l-1