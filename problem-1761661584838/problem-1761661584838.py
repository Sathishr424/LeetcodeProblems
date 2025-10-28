# Last updated: 28/10/2025, 7:56:24 pm
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = 0
        r = n-1
        score = 0
        while l < r:
            num = nums[r]
            dig = 1
            while num:
                num //= 10
                dig *= 10

            score += nums[l] * dig + nums[r]
            l += 1
            r -= 1

        if l == r:
            score += nums[l]
        return score