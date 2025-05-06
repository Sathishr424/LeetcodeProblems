# Last updated: 6/5/2025, 1:20:06 pm
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            nums[i] = (nums[nums[i]] % 1000) * 1000 + nums[i]

        for i in range(n):
            nums[i] = nums[i] // 1000
        
        return nums