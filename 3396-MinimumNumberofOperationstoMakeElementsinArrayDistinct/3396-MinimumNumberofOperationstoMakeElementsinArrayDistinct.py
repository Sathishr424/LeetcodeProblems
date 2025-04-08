# Last updated: 8/4/2025, 5:58:38 am
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        there = [0] * 101

        for i in range(len(nums)-1, -1, -1):
            if there[nums[i]]:
                return ceil((i+1) / 3)
            
            there[nums[i]] += 1
        
        return 0