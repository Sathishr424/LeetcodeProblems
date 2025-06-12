# Last updated: 12/6/2025, 5:40:18 am
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        ret = 0

        while left < right:
            tot = nums[left] + nums[right]

            if tot > k:
                right -= 1
            elif tot < k:
                left += 1
            else:
                ret += 1
                left += 1
                right -= 1
        
        return ret

