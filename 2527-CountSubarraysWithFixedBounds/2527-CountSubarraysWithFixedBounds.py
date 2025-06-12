# Last updated: 12/6/2025, 5:37:45 am
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        [1,3,5,2,7,5]
        [5,3,5,1,2,1,5,8,7,1,2,5,2]
        """

        prev = 0
        left = 0
        ret = 0
        mnk = 0
        mxk = 0

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                prev = 0
                left = i+1
                mnk = 0
                mxk = 0
                continue

            if num == minK: mnk += 1
            if num == maxK: mxk += 1

            while mnk > 0 and mxk > 0:
                if nums[left] == minK: mnk -= 1
                if nums[left] == maxK: mxk -= 1
                
                left += 1
                prev += 1
            
            ret += prev
        
        return ret