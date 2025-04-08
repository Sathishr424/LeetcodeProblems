# Last updated: 8/4/2025, 5:54:44 am
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        there = {}
        for i in range(n-1, -1, -1):
            if nums[i] not in there:
                there[nums[i]] = 1
            else:
                return ceil((i+1) / 3)
        
        return 0