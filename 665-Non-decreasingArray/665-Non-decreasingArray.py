# Last updated: 17/7/2025, 6:57:13 pm
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)

        count = 0
        for i in range(n-1):
            if nums[i] > nums[i + 1]:
                if i == 0:
                    count += 1
                else:
                    count += 1
                    if count > 1: return False
                    if i + 2 == n: return True
                    if nums[i + 2] < nums[i] and nums[i-1] > nums[i + 1]: return False
        
        return True