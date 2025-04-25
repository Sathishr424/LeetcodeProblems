# Last updated: 26/4/2025, 2:46:46 am
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ret = 0
        left = 0
        p = 1

        for i, num in enumerate(nums):
            p *= num
            
            if p >= k:
                while left <= i and p >= k:
                    p //= nums[left]
                    left += 1
            
            ret += i-left+1
        
        return ret