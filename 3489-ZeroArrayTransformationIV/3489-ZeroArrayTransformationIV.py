# Last updated: 13/6/2025, 10:32:11 pm
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def canMakeItZero(index):
            can = {}
            can[nums[index]] = 1
            for k, (x, y, val) in enumerate(queries):
                if x <= index and y >= index:
                    new_can = {}
                    for num in can:
                        new_can[num] = 1
                        if num-val >= 0:
                            if num-val == 0: return k + 1
                            new_can[num - val] = 1
                    can = new_can
            return -1
        
        ret = 0
        for i in range(len(nums)):
            if nums[i] == 0: continue

            index = canMakeItZero(i)
            if index == -1: return -1
            ret = max(ret, index)
        
        return ret