# Last updated: 20/5/2025, 4:47:33 pm
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        
        def rec(index, need):
            if need == 0: return -1
            sums = [False] * (need+1)
            sums[0] = True

            for i, (x, y, val) in enumerate(queries):
                if x <= index and y >= index and need-val >= 0:
                    if sums[need-val]: return i
                    for s in range(need-1, val-1, -1):
                        sums[s] = sums[s-val] or sums[s]
            return m
        
        ret = -1
        for i, num in enumerate(nums):
            ret = max(ret, rec(i, num))
        
        return -1 if ret >= m else ret+1
