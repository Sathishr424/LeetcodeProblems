# Last updated: 25/6/2025, 12:04:51 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        larger = 0

        for i in range(len(nums)):
            if i > larger: return False
            larger = cmax(larger, i + nums[i])
        
        return True
