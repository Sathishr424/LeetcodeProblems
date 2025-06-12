# Last updated: 12/6/2025, 5:40:23 am
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        n = len(nums)
        ret = []

        prefix = 0 
        for i, num in enumerate(nums):
            
            left = (num*i) - prefix
            prefix += num
            right = total - prefix - ((n-i-1) * num)

            ret.append( left + right )
        
        return ret