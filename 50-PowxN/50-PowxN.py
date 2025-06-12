# Last updated: 12/6/2025, 5:54:28 am
# 8 -> 4 -> 2 -> 1
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        def pow(x, n):
            if n == 1: return x
            ans = pow(x, n // 2)
            ans *= ans
            if n % 2: ans *= x
            return ans
        
        if n < 0: return pow(1/x, -n)
        return pow(x, n)