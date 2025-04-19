# Last updated: 19/4/2025, 5:01:25 pm
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        left = 0
        right = 0

        l = 0
        r = n-1
        while l < r:
            sum = nums[l] + nums[r]

            if sum < lower:
                left += r-l
                l += 1
            else:
                r -= 1
    
        l = 0
        r = n-1
        while l < r:
            sum = nums[l] + nums[r]

            if sum <= upper:
                right += r-l
                l += 1
            else:
                r -= 1
        
        return right-left
