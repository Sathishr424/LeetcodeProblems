# Last updated: 6/5/2025, 12:37:30 pm
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        
        return ans