# Last updated: 12/6/2025, 5:51:53 am
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ret = 0
        for bit in range(n.bit_length(), -1, -1):
            if m & (1 << bit) != n & (1 << bit): break
            else:
                ret |= m & (1 << bit)
        
        return ret
            