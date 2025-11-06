# Last updated: 6/11/2025, 4:05:58 pm
class Solution:
    def minOperations(self, n: int) -> int:
        if n == 0: return 0
        min_diff = inf

        for i in range(32):
            min_diff = min(min_diff, abs(n - (1 << i)))
        
        return self.minOperations(min_diff) + 1