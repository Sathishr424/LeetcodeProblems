# Last updated: 27/5/2025, 5:58:57 am
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s = n * (n+1) // 2

        x = m
        y = 0
        while x <= n:
            y += x
            x += m
        
        return (s - y) - y