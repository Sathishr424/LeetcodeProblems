# Last updated: 8/4/2025, 5:56:48 am
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        there = set()
        for i in range(n-1, -1, -1):
            if nums[i] in there:
                return ceil((i+1) / 3)
            
            there.add(nums[i])
        
        return 0