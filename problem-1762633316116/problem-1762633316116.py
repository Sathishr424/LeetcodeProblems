# Last updated: 9/11/2025, 1:51:56 am
class Solution:
    def coloredCells(self, n: int) -> int:
        return n * (n - 1) // 2 * 4 + 1