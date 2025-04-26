# Last updated: 26/4/2025, 9:07:50 am
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
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

            if num == minK:
                mnk += 1

            if num == maxK:
                mxk += 1

            if num < minK or num > maxK:
                prev = 0
                left = i+1
                mnk = 0
                mxk = 0
                continue

            while mnk > 0 and mxk > 0:
                num = nums[left]
                if num == minK:
                    mnk -= 1
                if num == maxK:
                    mxk -= 1
                
                left += 1
                prev += 1
            
            ret += prev
        
        return ret