# Last updated: 9/11/2025, 1:49:43 am
class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1: return 1
        ans = 1
        for i in range(1, n):
            ans += i * 4

        return ans