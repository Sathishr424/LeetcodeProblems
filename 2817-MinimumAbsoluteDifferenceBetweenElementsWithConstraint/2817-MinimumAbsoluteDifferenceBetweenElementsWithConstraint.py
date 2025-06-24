# Last updated: 24/6/2025, 2:40:03 pm
inf = float('inf')
class Solution:
    def findIndices(self, nums: List[int], indexDiff: int, valDiff: int) -> List[int]:
        mini = 0
        maxi = 0
        n = len(nums)

        for i in range(indexDiff, n):
            if nums[i - indexDiff] < nums[mini]:
                mini = i - indexDiff
            if nums[i - indexDiff] > nums[maxi]:
                maxi = i - indexDiff

            if abs(nums[i] - nums[mini]) >= valDiff:
                return [mini, i]
            elif abs(nums[maxi] - nums[i]) >= valDiff:
                return [maxi, i]
        
        return [-1, -1]