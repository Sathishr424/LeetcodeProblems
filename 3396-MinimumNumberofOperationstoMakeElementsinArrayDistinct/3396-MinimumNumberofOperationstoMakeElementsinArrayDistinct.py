# Last updated: 8/4/2025, 5:55:38 am
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        there = {}
        for i in range(n-1, -1, -1):
            if nums[i] in there:
                return ceil((i+1) / 3)
            
            there[nums[i]] = 1
        
        return 0