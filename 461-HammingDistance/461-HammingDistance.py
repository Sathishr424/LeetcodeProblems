# Last updated: 12/6/2025, 5:49:11 am
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        ret = 0
        while x:
            ret += x & 1 == 1
            x >>= 1
        
        return ret