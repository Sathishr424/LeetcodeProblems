# Last updated: 21/5/2025, 6:56:20 pm
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        left = 0
        right = 0

        l = 0
        r = n-1
        while l < r:
            if nums[l] + nums[r] < lower:
                left += r-l
                l += 1
            else:
                r -= 1
    
        l = 0
        r = n-1
        while l < r:
            if nums[l] + nums[r] <= upper:
                right += r-l
                l += 1
            else:
                r -= 1
        
        return right-left
