# Last updated: 14/5/2025, 8:41:08 pm
mod = 1337

def pow(x, n):
    if n == 1: return x
    ans = pow(x, n//2)
    ans = ans * ans % mod
    if n % 2: ans = ans * x % mod
    return ans

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # a^24 = (a^2)^10 * a^4
        # a^245 = ((a^2)^10 * a^4)^10 * a^5

        ret = 1
        for num in b:
            ret = pow(ret, 10)
            if num == 0: continue
            ret = ret * pow(a, num) % mod

        return ret