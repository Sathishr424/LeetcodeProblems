# Last updated: 15/4/2025, 4:43:54 pm
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        second_max = -1
        third_max = n-1

        for i in range(n-2, -1, -1):
            num = nums[i]
            if num >= nums[third_max]:
                third_max = i
            elif second_max == -1 or num >= nums[second_max]:
                second_max = i
            else:
                if second_max != -1 and num < nums[second_max]: return True
        
        return False
