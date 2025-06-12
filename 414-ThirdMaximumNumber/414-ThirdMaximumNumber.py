# Last updated: 12/6/2025, 5:49:39 am
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) <= 2: return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)