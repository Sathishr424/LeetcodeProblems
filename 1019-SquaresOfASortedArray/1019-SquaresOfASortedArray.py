# Last updated: 12/6/2025, 5:44:46 am
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i = 0
        while i < n and nums[i] < 0:
            i += 1
        
        j = i
        i -= 1
        ret = []

        while i >= 0 and j < n:
            if -nums[i] > nums[j]:
                ret.append(nums[j] * nums[j])
                j += 1
            else:
                ret.append(nums[i] * nums[i])
                i -= 1
        
        while i >= 0:
            ret.append(nums[i] * nums[i])
            i -= 1
        
        while j < n:
            ret.append(nums[j] * nums[j])
            j += 1
        
        return ret