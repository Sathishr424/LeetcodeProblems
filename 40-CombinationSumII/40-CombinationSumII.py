# Last updated: 4/8/2025, 11:37:40 pm
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        def rec(index, arr):
            if len(arr) == k:
                ret.append(arr[:])
                return
            
            for i in range(index, n + 1):
                arr.append(i)
                rec(i + 1, arr)
                arr.pop()
        rec(1, [])
        return ret