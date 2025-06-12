# Last updated: 12/6/2025, 5:47:38 am
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def decToBin(val, s=""):
            if val == 0: return s
            s = decToBin(val // 2, s)
            s += str(val % 2)
            return s
        
        prev = None
        for b in decToBin(n):
            if b == prev: return False
            prev = b
        return True