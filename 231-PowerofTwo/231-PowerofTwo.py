# Last updated: 9/8/2025, 7:30:37 am
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        
        while n > 1:
            if n % 2: return False
            n //= 2
        
        return True