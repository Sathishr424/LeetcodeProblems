# Last updated: 13/4/2025, 6:53:59 pm
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        
        neg = 1
        if x < 0: 
            x *= -1
            if n % 2 == 1: neg = -1
        
        def helper(n):
            if n == 0: return 1
            elif n == 1: return x

            ret = x*x
            i = 4
            prev = 2

            while i <= n:
                ret *= ret
                prev = i
                i += i

            return ret * helper(n - prev)
        return helper(n) * neg