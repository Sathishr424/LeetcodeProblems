# Last updated: 7/9/2025, 8:34:21 pm
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = []
        if n % 2:
            ret.append(0)
            n -= 1
        
        for i in range(n // 2):
            ret.append(i + 1)
        
        for i in range(n // 2):
            ret.append(-(i + 1))
        
        return ret