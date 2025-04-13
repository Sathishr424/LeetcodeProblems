# Last updated: 13/4/2025, 7:58:46 am
mod = 10 ** 9 + 7

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 0: return 1
        elif n == 1: return 5
        
        i = 4
        ret = 20
        prev = 2
        while i <= n:
            ret *= ret
            ret %= mod
            prev = i
            i += i
        
        return (ret * self.countGoodNumbers(n - prev)) % mod