# Last updated: 12/6/2025, 5:49:21 am
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash = {}
        ans = []

        for num in nums:
            hash[num] = 1
        
        for num in range(1, n+1):
            if num not in hash: ans.append(num)
        
        return ans
