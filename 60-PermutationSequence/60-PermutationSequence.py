# Last updated: 28/5/2025, 2:35:20 am
@cache
def fact(x):
    return factorial(x)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def rec(arr, k):
            if len(arr) == 1: return str(arr[0])
            prev = 0
            p = fact(len(arr) - 1)
            for i in range(len(arr)):
                if k <= prev + p:
                    return str(arr[i]) + rec(arr[:i] + arr[i+1:], k-prev)
                prev += p
        
        return rec([i for i in range(1, n+1)], k)