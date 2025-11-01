# Last updated: 1/11/2025, 10:21:06 pm
def fact(i, r):
    if i > r: return 1
    return i * fact(i + 1, r)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m:
            n, m = m, n
        n -= 1
        m -= 1
        
        return fact(m + 1, (m + n)) // factorial(n)