# Last updated: 12/4/2025, 9:55:33 pm
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1

        hash = {}

        for i in range(n):
            for j in range(i+1, n):
                hash[nums[i] ^ nums[j]] = 1
        
        ret = {}
        for num in hash:
            for x in nums:
                ret[x ^ num] = 1

        return len(ret)

        
        