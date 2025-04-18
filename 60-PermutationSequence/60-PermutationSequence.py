# Last updated: 19/4/2025, 3:33:13 am
@cache
def fact(x):
    if x <= 1: return 1
    return fact(x-1) * x

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def helper(arr, k):
            n = len(arr)
            prev = 0
            fa = fact(n-1)

            for i in range(n):
                f = prev+fa
                if f >= k:
                    return str(arr[i]) + helper(arr[:i] + arr[i+1:], k-prev)
                prev = f
            
            return ''
        
        return helper([i for i in range(1, n+1)], k)