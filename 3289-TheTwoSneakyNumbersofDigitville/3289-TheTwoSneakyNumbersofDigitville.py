# Last updated: 31/10/2025, 3:21:32 pm
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        ret = []
        for num in nums:
            if num in seen:
                ret.append(num)
            else:
                seen.add(num)
        
        return ret