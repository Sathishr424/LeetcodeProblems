# Last updated: 12/6/2025, 5:33:08 am
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        return max(0, n-k) * k + max(0, m-k) * k