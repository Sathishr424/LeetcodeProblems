# Last updated: 27/5/2025, 6:12:16 am
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s = n * (n+1) // 2

        y = n // m
        y = (y * (y+1) // 2) * m

        return (s - y) - y