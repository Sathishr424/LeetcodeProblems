# Last updated: 9/8/2025, 7:45:24 am
maxi = (1 << 31) - 1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0