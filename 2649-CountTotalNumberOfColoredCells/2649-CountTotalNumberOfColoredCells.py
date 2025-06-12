# Last updated: 12/6/2025, 5:37:23 am
class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 5

        # a = 3
        # formula = (((a+0) * 4) - 4 ) + (((a+1) * 4) - 4) .... (((a+n) * 4) - 4)

        right = n*(n+1)*4/2
        n -= 2
        
        return int(right-12-(4*n)) + 5