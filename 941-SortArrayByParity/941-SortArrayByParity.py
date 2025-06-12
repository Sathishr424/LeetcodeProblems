# Last updated: 12/6/2025, 5:45:27 am
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x:  x % 2)