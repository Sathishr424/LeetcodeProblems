# Last updated: 20/5/2025, 4:01:47 pm
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        
        def rec(index, need):
            there = {0: 0}
            for i, (x, y, val) in enumerate(queries):
                if x <= index and y >= index and need-val >= 0:
                    new_there = {}
                    for num in there:
                        new_there[num] = there[num]
                        if num+val == need: return i
                        new_there[num + val] = i
                    there = new_there
            return m
        
        ret = -1
        for i, num in enumerate(nums):
            if num == 0: continue
            ret = max(ret, rec(i, num))
        
        return -1 if ret >= m else ret+1
            


