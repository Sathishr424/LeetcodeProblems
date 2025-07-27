# Last updated: 27/7/2025, 10:20:23 am
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)

        ret = 0
        for i in range(1, n-1):
            if nums[i] == nums[i-1]: continue
            left = i-1
            right = i+1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            while right < n and nums[right] == nums[i]:
                right += 1
            
            if left >= 0 and right < n:
                if nums[left] < nums[i] and nums[right] < nums[i]:
                    ret += 1
                elif nums[left] > nums[i] and nums[right] > nums[i]:
                    ret += 1
            
        return ret