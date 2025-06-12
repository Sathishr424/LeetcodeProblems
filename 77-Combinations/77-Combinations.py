# Last updated: 12/6/2025, 5:53:50 am
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def rec(i, j, arr):
            if i == k: return ret.append(arr + [])

            for l in range(j, n+1):
                arr.append(l)
                rec(i+1, l+1, arr)
                arr.pop()
        
        rec(0, 1, [])
        return ret