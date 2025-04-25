# Last updated: 26/4/2025, 2:47:15 am
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ret = 0
        left = 0
        p = 1

        for i, num in enumerate(nums):
            p *= num
            
            while p >= k and left <= i:
                p //= nums[left]
                left += 1
            
            ret += i-left+1
        
        return ret