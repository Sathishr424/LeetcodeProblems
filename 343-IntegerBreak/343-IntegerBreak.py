# Last updated: 12/6/2025, 5:50:20 am
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        ret = 1
        while n >= 5:
            n -= 3
            ret *= 3
        return ret * n