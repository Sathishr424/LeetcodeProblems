# Last updated: 12/6/2025, 5:51:59 am
class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0

        for i in range(32):
            num = (num << 1) | (n & 1)
            n >>= 1
        
        return num