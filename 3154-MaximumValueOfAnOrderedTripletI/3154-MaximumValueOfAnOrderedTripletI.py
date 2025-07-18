# Last updated: 12/6/2025, 5:36:08 am
inf = float('inf')

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ret = 0
        
        first = -float('inf')
        second = -float('inf')

        for i in range(len(nums)):
            ret = max(second * nums[i], ret)

            second = max(first - nums[i], second)
            first = max(first, nums[i])

        
        return ret if ret > 0 else 0
