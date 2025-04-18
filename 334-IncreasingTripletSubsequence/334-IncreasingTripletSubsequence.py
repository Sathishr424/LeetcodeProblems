# Last updated: 15/4/2025, 4:49:08 pm
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        second_max = -1
        third_max = n-1

        for i in range(n-2, -1, -1):
            if nums[i] >= nums[third_max]:
                third_max = i
            elif second_max == -1 or nums[i] >= nums[second_max]:
                second_max = i
            else: return True
        
        return False
