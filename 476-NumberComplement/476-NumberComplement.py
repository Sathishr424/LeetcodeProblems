# Last updated: 12/6/2025, 5:49:07 am
class Solution:
    def decToBin(self, x, s=0, index=0):
        if x == 0: return s
        s += (x % 2 == 0) * (2 ** index)
        s = self.decToBin(x // 2, s, index+1)
        return s
    
    def findComplement(self, num: int) -> int:
        return self.decToBin(num)

