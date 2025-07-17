# Last updated: 17/7/2025, 6:54:02 pm
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        okay_right = [1] * n

        for i in range(n-2, -1, -1):
            if okay_right[i + 1] == 0 or nums[i] > nums[i + 1]:
                okay_right[i] = 0
            
        for i in range(n-1):
            if nums[i] > nums[i + 1]:
                if i == 0:
                    if okay_right[i + 1]: return True
                    return False
                else:
                    if not okay_right[i + 1]: return False
                    if i + 2 == n: return True
                    if nums[i + 2] < nums[i] and nums[i-1] > nums[i + 1]: return False
                    return True
        
        return True