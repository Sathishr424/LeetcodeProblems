# Last updated: 12/6/2025, 5:44:19 am
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0
        ret = []
        index = len(nums)-1
        for num in nums:
            if num: val += 2**index
            index -= 1
            ret.append(val % 5 == 0)
        return ret