# Last updated: 12/6/2025, 5:42:04 am
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] > nums[j]: ret[i]+=1
        return ret
        