# Last updated: 12/6/2025, 5:39:33 am
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def rec(index, xor):
            if index == n: return xor
            return rec(index+1, xor ^ nums[index]) + rec(index+1, xor)
        
        return rec(0, 0)