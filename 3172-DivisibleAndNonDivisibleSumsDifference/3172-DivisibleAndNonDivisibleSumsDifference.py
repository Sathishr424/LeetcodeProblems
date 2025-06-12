# Last updated: 12/6/2025, 5:36:05 am
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n * (n+1) // 2 - n // m * (n // m+1) * m