# Last updated: 13/4/2025, 7:53:04 am
mod = 10 ** 9 + 7

class Solution:
    @cache
    def countGoodNumbers(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 5
        elif n == 2: return 20
        elif n == 3: return 100
        
        i = 4
        curr = 20
        prev = 2
        while i <= n:
            curr *= curr
            curr %= mod

            prev = i
            i += i
        
        diff = n - prev
        return (curr * self.countGoodNumbers(diff)) % mod