# Last updated: 20/5/2025, 4:26:18 pm
cmin = lambda x, y: x if x < y else y
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        
        def rec(index, need):
            sums = [m] * (need+1)
            sums[0] = 0

            for i, (x, y, val) in enumerate(queries):
                if x <= index and y >= index:
                    for j in range(need-val, -1, -1):
                        if sums[j] < m:
                            if j+val == need: return i
                            sums[j+val] = cmin(sums[j+val], i)
            return sums[need]
        
        ret = -1
        for i, num in enumerate(nums):
            if num == 0: continue
            ret = max(ret, rec(i, num))
        
        return -1 if ret >= m else ret+1
