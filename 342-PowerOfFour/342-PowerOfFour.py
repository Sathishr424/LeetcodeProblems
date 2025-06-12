# Last updated: 12/6/2025, 5:50:22 am
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        ans = 1
        while ans < n:
            ans *= 4
        return ans == n