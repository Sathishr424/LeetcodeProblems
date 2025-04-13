# Last updated: 13/4/2025, 7:09:52 pm
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        
        @cache
        def rec(n):
            if n == 0: return 1
            elif n == 1: return x

            if n % 2 == 0:
                return rec(n//2) * rec(n//2)
            else:
                return rec(n//2) ** 2 * x
        
        return rec(n)