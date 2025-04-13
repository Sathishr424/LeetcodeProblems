# Last updated: 13/4/2025, 7:11:14 pm
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        
        def rec(n):
            if n == 0: return 1
            elif n == 1: return x

            ans = rec(n//2)
            
            if n % 2 == 0:
                return ans * ans
            else:
                return ans * ans * x
        
        return rec(n)