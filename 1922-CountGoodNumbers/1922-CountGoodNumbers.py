# Last updated: 17/6/2025, 8:10:25 pm
mod = 10 ** 9 + 7

@cache
def cPow(x, n):
    if n == 0: return 1
    if n == 1: return x
    half = n // 2

    ans = cPow(x, half)
    ans = ans * ans % mod

    return ans * (x if n % 2 else 1)

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return cPow(5, (n + 1) // 2) * cPow(4, n // 2) % mod