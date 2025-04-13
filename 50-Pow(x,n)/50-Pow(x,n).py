# Last updated: 13/4/2025, 7:41:55 pm
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        
        def rec(n):
            if n == 0: return 1

            ans = rec(n//2)
            ans *= ans
            
            return ans * x if n % 2 else ans
        
        return rec(n)