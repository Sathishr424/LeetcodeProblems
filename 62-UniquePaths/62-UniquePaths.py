# Last updated: 1/11/2025, 10:12:40 pm
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2) // (factorial(n-1) * factorial(m-1))