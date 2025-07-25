# Last updated: 12/6/2025, 5:35:48 am
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] == nums[1] and nums[1] == nums[2]:
            return "equilateral"

        nums.sort()
        if nums[0] + nums[1] > nums[2]:
            s = {}
            s[nums[0] + nums[1]] = 1
            s[nums[1] + nums[2]] = 1
            s[nums[2] + nums[0]] = 1

            if len(s) == 3: return 'scalene'
            return 'isosceles'

        return 'none'

