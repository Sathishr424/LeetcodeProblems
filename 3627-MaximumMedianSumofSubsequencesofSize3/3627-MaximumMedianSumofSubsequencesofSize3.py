# Last updated: 28/7/2025, 9:24:53 pm
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)

        need = len(nums) // 3
        ret = 0

        while need:
            nums.pop()
            ret += nums.pop()
            need -= 1
        
        return ret