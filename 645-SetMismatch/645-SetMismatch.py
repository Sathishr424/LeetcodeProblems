# Last updated: 12/6/2025, 5:47:58 am
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)

        val = (n*(n+1))//2
        
        hash = {}

        for num in nums:
            if num in hash: return [num, val-(total-num)]
            hash[num] = 1