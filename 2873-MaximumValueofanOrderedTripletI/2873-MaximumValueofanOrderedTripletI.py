# Last updated: 2/4/2025, 4:50:55 pm
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        ret = 0
        second = -float('inf')
        first = -float('inf')

        for i in range(n):
            ret = max(ret, second * nums[i])
            second = max(second, first - nums[i])
            first = max(first, nums[i])
        
        return ret