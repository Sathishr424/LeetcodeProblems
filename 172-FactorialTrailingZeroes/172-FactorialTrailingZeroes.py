# Last updated: 12/6/2025, 5:52:06 am
class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 5
        ans = 0
        while i <= n:
            ans += n//i
            i *= 5
        return ans
        