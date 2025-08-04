# Last updated: 5/8/2025, 12:21:58 am
class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2 * n) // (factorial(n + 1) * factorial(n))