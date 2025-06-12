# Last updated: 12/6/2025, 5:38:01 am
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] < nums[i]:
                steps = (nums[i]-1)//nums[i+1]
                nums[i] = nums[i]//(steps+1)
                ret += steps
        return ret