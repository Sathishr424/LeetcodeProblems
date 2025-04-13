# Last updated: 13/4/2025, 7:46:50 pm
mod = 10 ** 9 + 7

def pow(x, n):
    if n == 0: return 1

    ans = pow(x, n // 2)
    ans = ans * ans % mod

    return ans * x % mod if n % 2 else ans

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evens = (n + 1) // 2
        odds = n // 2

        return pow(5, evens) * pow(4, odds) % mod