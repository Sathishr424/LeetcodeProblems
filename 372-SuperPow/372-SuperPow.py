# Last updated: 13/4/2025, 8:53:06 pm
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337

        @cache
        def pow(x, n):
            if n == 0: return 1
            elif n == 1: return x

            ans = pow(x, n//2)
            
            if n % 2 == 0:
                return ans * ans % mod
            else:
                ans = ans * ans % mod
                return ans * x % mod
        
        ret = 1

        for n in b:
            ret = pow(ret, 10) * pow(a, n) % mod

        return ret


        