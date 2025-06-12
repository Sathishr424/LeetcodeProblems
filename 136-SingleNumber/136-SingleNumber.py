# Last updated: 12/6/2025, 5:52:32 am
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = nums[0]

        for i in range(1, len(nums)):
            num ^= nums[i]
        
        return num