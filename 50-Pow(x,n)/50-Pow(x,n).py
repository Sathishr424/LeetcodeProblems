# Last updated: 13/4/2025, 7:09:18 pm
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
                ans = rec(n//2) * rec(n//2)
            else:
                ans = rec(n//2) * rec(n//2) * x
            
            return ans
        
        return rec(n)