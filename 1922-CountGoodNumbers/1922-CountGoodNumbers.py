# Last updated: 13/4/2025, 9:27:56 am
mod = 10 ** 9 + 7

@cache
def good(n):
    if n == 0: return 1
    elif n == 1: return 5
    
    i = 4
    ret = 20
    prev = 2
    while i <= n:
        ret = ret * ret % mod
        prev = i
        i += i
    
    return (ret * good(n - prev)) % mod

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return good(n)