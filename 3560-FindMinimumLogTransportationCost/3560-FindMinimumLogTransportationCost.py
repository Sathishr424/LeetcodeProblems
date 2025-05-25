# Last updated: 25/5/2025, 9:37:43 am
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        return max(0, n-k) * k + max(0, m-k) * k