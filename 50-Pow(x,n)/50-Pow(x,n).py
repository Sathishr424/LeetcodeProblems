# Last updated: 5/8/2025, 5:44:33 pm
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def cPow(num, power):
            if power == 0: return 1
            if power == 1: return num
            half = power // 2
            ans = cPow(num, half)
            ans = ans * ans
            if power % 2:
                ans = ans * num
            return ans
        
        if n < 0:
            return cPow(1/x, -n)
        return cPow(x, n)
