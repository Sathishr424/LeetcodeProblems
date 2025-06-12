# Last updated: 12/6/2025, 5:47:07 am
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = max(nums)
        index = 0

        for i, num in enumerate(nums):
            if num == maxi:
                index = i
            elif num*2 > maxi: 
                return -1
        
        return index