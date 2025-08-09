# Last updated: 9/8/2025, 7:34:50 am
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0