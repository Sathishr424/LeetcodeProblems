# Last updated: 11/8/2025, 11:31:01 am
mod = 10 ** 9 + 7
def inverse(x):
    return pow(x, mod - 2, mod)

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = deque([])
        prefix = [1]

        for i in range(31, -1, -1):
            if n >= (1 << i):
                curr = pow(2, i, mod)
                arr.appendleft(curr)
                n -= curr
        
        for i in range(len(arr)):
            prefix.append(prefix[-1] * arr[i] % mod)
        
        ret = []
        for l, r in queries:
            ret.append(prefix[r + 1] * inverse(prefix[l]) % mod)
        
        return ret
