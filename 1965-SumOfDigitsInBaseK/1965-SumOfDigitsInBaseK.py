# Last updated: 12/6/2025, 5:39:41 am
class Solution:
    def convertBase(self, n, b, rem=''):
        if n == 0: return str(rem[::-1])
        return self.convertBase(n//b, b, rem + str(n%b))
    
    def sumBase(self, n: int, k: int) -> int:
        b = self.convertBase(n, k)
        return sum((map(int, b)))