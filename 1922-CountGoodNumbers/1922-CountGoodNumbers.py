# Last updated: 17/6/2025, 8:04:47 pm
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1: return 5
        mod = 10 ** 9 + 7

        ret = pow(5, n//2, mod)
        ret = ret * pow(4, n//2, mod) % mod
        if n % 2:
            ret = ret * 5 % mod
        return ret