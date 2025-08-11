# Last updated: 11/8/2025, 2:17:33 pm
mod = 10 ** 9 + 7
def inverse(x):
    return pow(x, -1, mod)

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        prefix = [0]

        for i in range(32):
            if n & (1 << i) > 0:
                prefix.append(prefix[-1] + i)
        
        ret = []
        for l, r in queries:
            ret.append(pow(2, prefix[r + 1] - prefix[l], mod))
        
        return ret
