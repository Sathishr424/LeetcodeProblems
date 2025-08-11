# Last updated: 11/8/2025, 11:39:06 am
mod = 10 ** 9 + 7
def inverse(x):
    return pow(x, -1, mod)

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = []
        prefix = [1]

        for i in range(32):
            if n & (1 << i) > 0:
                curr = 1 << i
                arr.append(curr)
                prefix.append(prefix[-1] * curr % mod)
        
        ret = []
        for l, r in queries:
            ret.append(prefix[r + 1] * inverse(prefix[l]) % mod)
        
        return ret
