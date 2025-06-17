# Last updated: 17/6/2025, 8:01:15 pm
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1: return 5
        mod = 10 ** 9 + 7

        def calc(m, val):
            if m == 1: return val

            half = m // 2
            ans = calc(half, val)
            ans = ans * ans % mod

            if m % 2:
                ans = ans * val % mod

            return ans
        
        ret = calc(n//2, 5)
        ret = ret * calc(n//2, 4) % mod
        if n % 2:
            ret = ret * 5 % mod
        return ret