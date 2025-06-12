# Last updated: 12/6/2025, 5:53:46 am
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 0
        cnt = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                cnt += 1
                if cnt <= 2: r += 1
            else:
                cnt = 1
                r += 1
            prev = nums[i]
            nums[r] = nums[i]
        
        return r+1
        
