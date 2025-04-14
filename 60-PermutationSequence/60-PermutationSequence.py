# Last updated: 14/4/2025, 8:19:51 pm
@cache
def fact(x):
    if x <= 1: return x
    return fact(x-1) * x

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def arrToSt(arr):
            return ''.join([str(i) for i in arr])

        def rec(arr, k):
            m = len(arr)
            prev = 0

            for i in range(m):
                x = fact(m-1) + prev
                if x >= k:
                    new_arr = arr[:i] + arr[i+1:]
                    if x == k: return str(arr[i]) + arrToSt(sorted(new_arr, reverse=True))
                    return str(arr[i]) + rec(new_arr, k-prev)
                prev = x
            
            return str(arr[0])

        return rec([i for i in range(1, n+1)], k)
