# Last updated: 27/5/2025, 6:19:16 am
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n * (n+1) // 2 - n // m * (n // m+1) * m