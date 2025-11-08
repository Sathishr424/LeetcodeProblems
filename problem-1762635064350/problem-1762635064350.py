# Last updated: 9/11/2025, 2:21:04 am
N = 10**5 + 1
fact = [1] * N
mod = 10**9 + 7

for i in range(1, N):
    fact[i] = fact[i - 1] * i % mod

inv_fact = [1] * N
inv_fact[N-1] = pow(fact[N-1], mod - 2, mod)

for i in range(N-2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
def ncr(n, k):
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def comb(n, k):
    return fact[n] * inv_fact[k] % mod
    
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        ranges.sort()
        n = len(ranges)
        # print(ranges)
        prev = ranges[0]
        cnt = 0
        for i in range(1, n):
            curr = ranges[i]
            if curr[0] > prev[1]: cnt += 1
            prev = [prev[0], max(prev[1], curr[1])]
            
        # print(cnt)
        ans = 0
        for i in range(1, cnt + 1):
            ans = (ans + ncr(cnt, i)) % mod

        return (ans * 2 % mod + 2) % mod

        