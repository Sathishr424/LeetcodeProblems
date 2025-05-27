# Last updated: 27/5/2025, 6:17:53 am
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n * (n+1) // 2 - n // m * (n // m+1) // 2 * m * 2