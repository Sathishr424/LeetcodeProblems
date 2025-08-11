# Last updated: 11/8/2025, 11:38:24 am
mod = 10 ** 9 + 7
def inverse(x):
    return pow(x, mod - 2, mod)

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = []

        for i in range(32):
            if n & (1 << i) > 0:
                curr = 1 << i
                arr.append(curr)

        ret = []
        for l, r in queries:
            ans = 1
            for i in range(l, r + 1):
                ans = ans * arr[i] % mod
            ret.append(ans)
        
        return ret
