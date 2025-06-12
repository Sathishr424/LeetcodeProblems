# Last updated: 12/6/2025, 5:50:34 am
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return True if n == 1 or n == 3 else (self.isPowerOfThree(n/3) if n >= 3 else False)