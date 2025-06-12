# Last updated: 12/6/2025, 5:36:17 am
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        m = abs(fx-sx)
        n = abs(fy-sy)
        if m == n and m == 0 and t == 1: return False
        return max(m, n) <= t
