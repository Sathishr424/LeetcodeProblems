# Last updated: 12/6/2025, 5:43:26 am
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(0,len(nums),2):
            ret += [nums[i+1]]*nums[i]
        return ret