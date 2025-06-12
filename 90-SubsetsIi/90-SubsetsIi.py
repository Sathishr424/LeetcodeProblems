# Last updated: 12/6/2025, 5:53:32 am
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)
        nums.sort()
        def rec(index, arr):
            ret.append(list(arr))
            prev = None
            for i in range(index, n):
                if nums[i] == prev: continue
                prev = nums[i]
                arr.append(nums[i])
                rec(i+1, arr)
                arr.pop()
        
        rec(0, [])
        return ret