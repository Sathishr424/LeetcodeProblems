# Last updated: 17/6/2025, 8:05:44 pm
mod = 10 ** 9 + 7
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return pow(5, (n + 1) // 2, mod) * pow(4, n // 2, mod) % mod