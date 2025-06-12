# Last updated: 12/6/2025, 5:36:10 am
_max = lambda x, y: x if x > y else y

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ret = 0
        second = -float('inf')
        first = -float('inf')

        for i in range(len(nums)):
            ret = _max(ret, second * nums[i])
            second = _max(second, first - nums[i])
            first = _max(first, nums[i])
        
        return ret