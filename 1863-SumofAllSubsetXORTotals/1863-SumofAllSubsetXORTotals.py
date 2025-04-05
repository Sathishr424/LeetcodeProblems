# Last updated: 5/4/2025, 3:53:01 pm
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def rec(index, xor):
            if index == n: return xor
            return rec(index+1, xor ^ nums[index]) + rec(index+1, xor)
        
        return rec(0, 0)