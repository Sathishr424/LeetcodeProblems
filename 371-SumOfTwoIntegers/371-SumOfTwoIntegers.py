# Last updated: 12/6/2025, 5:50:09 am
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
            xor = a ^ b
            b = (a & b) << 1
            a = xor
        
        return (a & mask) if b > 0 else a

