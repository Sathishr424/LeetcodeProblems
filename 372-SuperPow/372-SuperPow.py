# Last updated: 13/4/2025, 8:56:14 pm
mod = 1337

@cache
def pow(x, n):
    if n == 0: return 1

    ans = pow(x, n//2)
    ans = ans * ans % mod
    
    return ans * x % mod if n % 2 else ans

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ret = 1

        for n in b:
            ret = pow(ret, 10) * pow(a, n) % mod

        return ret


        