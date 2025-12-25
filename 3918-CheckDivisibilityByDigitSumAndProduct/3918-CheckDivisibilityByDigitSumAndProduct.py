# Last updated: 12/25/2025, 7:10:47 PM
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        orig = n
        s = 0
        p = 1
        while n:
            rem = n % 10
            s += rem
            p *= rem
            n //= 10
        
        return orig % (s + p) == 0