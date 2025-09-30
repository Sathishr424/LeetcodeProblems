# Last updated: 30/9/2025, 7:26:29 am
class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        while len(nums) > 1:
            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()
        
        return nums[0]