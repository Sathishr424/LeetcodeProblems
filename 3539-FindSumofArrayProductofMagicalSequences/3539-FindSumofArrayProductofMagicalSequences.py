# Last updated: 12/10/2025, 8:06:47 pm
N = 101
fact = [1] * N
mod = 10**9 + 7

for i in range(1, N):
    fact[i] = fact[i - 1] * i % mod

inv_fact = [1] * N
inv_fact[N-1] = pow(fact[N-1], mod - 2, mod)

for i in range(N-2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7

        @cache
        def rec(index, set_bits, next, rem):
            if rem == 0:
                # print(set_bits, next)
                while next:
                    set_bits += next % 2
                    next //= 2
                if set_bits == k: return 1
                return 0
            if index == n: return 0

            ans = rec(index + 1, set_bits + (next % 2), next // 2, rem)
            for i in range(1, rem + 1):
                ans += rec(index + 1, set_bits + ((next + i) % 2), (next + i) // 2, rem - i) * (nums[index] ** i) % mod * inv_fact[i] % mod
                ans %= mod

            return ans % mod
        
        ans = rec(0, 0, 0, m) * fact[m] % mod
        rec.cache_clear()
        return ans