# Last updated: 12/6/2025, 5:41:56 am
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.insert(index[i],nums[i])
        return ret