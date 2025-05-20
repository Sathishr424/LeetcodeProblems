# Last updated: 20/5/2025, 4:40:05 pm
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        
        def rec(index, need):
            sums = [False] * (need+1)
            sums[0] = True

            for i, (x, y, val) in enumerate(queries):
                if x <= index and y >= index:
                    for s in range(need-val, -1, -1):
                        if sums[s]:
                            if s+val == need: return i
                            sums[s+val] = True
            return m
        
        ret = -1
        for i, num in enumerate(nums):
            if num == 0: continue
            ret = max(ret, rec(i, num))
        
        return -1 if ret >= m else ret+1
