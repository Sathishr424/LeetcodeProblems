# Last updated: 12/6/2025, 5:51:17 am
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return True if n & (n-1) == 0 else False