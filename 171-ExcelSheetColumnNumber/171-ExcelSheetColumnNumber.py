# Last updated: 12/6/2025, 5:52:07 am
class Solution:
    def titleToNumber(self, col: str) -> int:
        n = len(col)
        
        ans = ord(col[-1])-64
        for i in range(n-1):
            ans += (ord(col[i])-64) * (26 ** (n-(i+1)))

        return ans